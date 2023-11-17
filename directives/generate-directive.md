# Build a Directive to accomplish the given Task

_.Build a Talkdown Directive to accomplish the task outlined at the end of this document._

## Input

This directive is given the description of a task to accomplish within the `description` input field. The directive should generate a directive that, when executed by a LLM along with the appropriate inputs, will accomplish the task described in the description.

### Required Input Fields

ONLY generate the directive if the following inputs are provided along with the task. If any of the following inputs are not provided, the task should fail.

* `name` - The name of the directive
* `description` - A description of the directive

### Optional Input Fields

* `author` - The author of the directive
* `version` - The version of the directive
* `license` - The license of the directive
* `tags` - A list of tags to associate with the directive
* `parameters` - A list of parameters to associate with the directive
* `output` - A list of outputs to associate with the directive
* `dependencies` - A list of dependencies to associate with the directive
* `examples` - A list of examples to associate with the directive

## Execution

This directive should generate a directive, formatted in Markdown, which when executed by a LLM along with the appropriate inputs, will accomplish the task described in the description.

The Directive must contain the following information:

The name of the directive will be used as the title of the directive. A description of the directive will be shown as the body of the directive.

The document should have the following sections:

* `Input` - A list of parameters to associate with the directive
* `Execution` - A description of the process to perform
* `Output` - The fields to output from the directive

## Output

This directive outputs a directive, formatted in Markdown, which when executed by a LLM along with the appropriate inputs, will accomplish the task described in the description.

### Required Output Fields

The directive must contain the following information:

* `name` - The name of the directive
* `description` - A description of the directive

### Optional Output Fields

* `author` - The author of the directive
* `version` - The version of the directive
* `tags` - A list of tags to associate with the directive
* `parameters` - A list of parameters to associate with the directive
* `output` - A list of outputs to associate with the directive
* `dependencies` - A list of dependencies to associate with the directive
* `examples` - A list of examples to associate with the directive
