---
title: Directive title
inputs: [filenames, folders, urls, etc.]
outputs: [Markdown, JSON, text, filename, folder, image, etc.]
folder: /Users/sschepis/Development/intellibiz
---

## Inputs

A line-item list of the expected inputs to the directive.

## Task

A summary of the task to be performed by the directive.

## Execution

```python
# python code to execute the 
def execute(inputs): # pass a dictionary of inputs from the inputs section
    pass
```

or

```ai
A prompt the AI executing this directive will use to self-prompt to execute the task.
```

## Output

A line-item list of the expected outputs from the directive. Should include the type of output and a description of the output.

Instruct the AI to output the following:
"End your output with routing information: {name of next directive, or condition}""

## Routing

A description of how to route the output of the directive to the next directive or condition. Can be as simple as specifying the name of the next directive, or as complex as a conditional statement, python code, or AI prompt.
