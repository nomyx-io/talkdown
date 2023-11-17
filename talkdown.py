import tiktoken
import mistletoe
import interpreter
from mistletoe.ast_renderer import AstRenderer
from mistletoe.markdown_renderer import MarkdownRenderer
import os
import time
interpreter.auto_run = True

def count_tokens(text):
    tokenizer = tiktoken.encoding_for_model("gpt-4")
    return sum(1 for _ in tokenizer.encode(text))

def _call_interpreter(q):
    try:
      response = interpreter.chat(q)
      return response[-1:][0]['message']
    except:
      # if this is a 429 then we need to wait the specified time
      # and then try again
      if response.status_code == 429:
        print('Rate limited. Retrying in %s seconds' % response.headers['Retry-After'])
        time.sleep(response.headers['Retry-After'])
        return _call_interpreter(q)
      else:
         return 'Error: ' + str(response.status_code)

# read all the documents of a folder and its subfolders
def load_documents(folder):
    """
    Load all the Talkdown documents from the file system.
    """
    documents = {}
    # get the current directory
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # get the directory of the folder
    folder = os.path.join(current_dir, folder)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as auto:
                    documents[file[:-3]] = auto.read()
    return documents

documents = load_documents("researcher")

def parse_talkdown(talkdown_content):
   with AstRenderer() as renderer:
      return renderer.render(mistletoe.Document(talkdown_content))

def prepare_prompt(current_document):
   return current_document

def process_response(response):
   # parse the document looking for 'Routing:' section and take everything to end of line after that
   parsed_response = response.split('Routing:')
   pre_parsed_response = parsed_response[0]

   parsed_response = parsed_response[1] if len(parsed_response) > 1 else ''
   parsed_response = parsed_response.split('\n')[0]
   parsed_response = parsed_response.strip()

   maybe_split = pre_parsed_response.split('```markdown')
   if len(maybe_split) > 1:
      # look for ```markdown and ``` and take everything in between
      pre_parsed_response = pre_parsed_response.split('```markdown')[1]
      pre_parsed_response = pre_parsed_response.split('```')[0]
   return {
       'response': pre_parsed_response,
       'next': parsed_response
   }

def load_talkdown_document(document_name):
   return documents[document_name]

def process_talkdown(file_name, file_loader):
    persona = """You are an advanced, autonomous AI capable of a vast array of capabilities and tasks. 
You are a part of a larger system that is responsible for processing Talkdown documents. This larger 
system wull always come to your aid should you face any task which seems beyond your capabilities.
If you are asked to perform something which you are not capable of, you should presume that you are
a part of a larger system and that you will be provided with the necessary capabilities to complete
the task.
You are currently deployed as a Talkdown processing agent. You process the following Talkdown document 
according to the specified conventions and execute the tasks outlined in it. Follow these steps carefully:

1. **Read the Metadata Header**
   - Identify the document's title, purpose, and list of inputs and outputs. 
   - Note these details for reference during task execution.

2. **Parse the Inputs Section**
   - Review the detailed descriptions and sources of each input.
   - Ensure all necessary inputs are available before proceeding.

3. **Understand the Task Description**
   - Read and comprehend the task summary and additional details.
   - If the task is ambiguous or unclear, ask for clarification.

4. **Execute the Task in the Execution Section**
   - For embedded code:
     - Run the code snippet and observe the output. If the code is in a language you can execute, simulate the execution and describe the expected outcome.
   - For AI prompts:
     - Respond to the AI prompt as accurately and effectively as possible, within your capabilities.

5. **Handle the Output Processing**
   - Extract the necessary data from the task's results.
   - Format the output as specified in the document. Ensure it meets the outlined requirements.

6. **Follow the Routing Information**
   - Determine the next Talkdown document to execute, based on the routing instructions.
   - If there are conditions attached to the routing, evaluate these conditions based on the current output and context.

7. **Error Handling**
   - If you encounter errors or issues in any step, report them clearly.
   - Provide suggestions or alternative actions if possible.

8. **Feedback and Logging**
   - Throughout the process, provide feedback on your actions and decisions.
   - Maintain a log of steps taken and outcomes for review.

Remember, your goal is to process the Talkdown document as if you were a part of an automated system, handling tasks, and transitioning between different stages of the workflow. Your responses should be precise, based on the information given in the document, and adhere to the Talkdown conventions, as they will be fed into an LLM for processing to drive the workflow.

```

"""
    def structured_command(query):
        p = persona + '\n' + prepare_prompt(query)
        retval = _call_interpreter(p)
        return retval.strip()

    # Step 1: Parse the Talkdown document
    current_document = file_loader(file_name)
    current_response = None
    final_response = None

    while current_document is not None:
        # Step 3: Call the LLM
        llm_request = current_document
        if(current_response is not None):
            llm_request = current_document + '\n\n INPUT DATA: ' + current_response
        response = structured_command(llm_request)

        # Step 4: Process the response
        # Extract relevant information (task results, outputs, routing info, etc.)
        processed_response = process_response(response)
        next_document_name = processed_response['next']
        current_response = processed_response['response'].strip()

        if next_document_name:
            # remove the .md extension if it is present
            if next_document_name.endswith('.md'):
                next_document_name = next_document_name[:-3]
            # Load the content of the next Talkdown document
            next_document_content = file_loader(next_document_name)
            current_document = next_document_content
        else:
            # End of workflow
            final_response = processed_response
            current_document = None

    # Step 5: Return the final response
    return final_response




# we are gonna load all markdown files in the current directory 
cwd = os.getcwd()
documents = load_documents(cwd)

def load_talkdown_document(document_name):
   return documents[document_name]


# and we are gonna run the file given on the command line
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: talkdown.py <filename>')
        sys.exit(1)
    filename = sys.argv[1]
    print(process_talkdown(filename, load_talkdown_document)['response'])