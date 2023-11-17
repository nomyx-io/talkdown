---
title: Talkdown Directive Template
description: A template for creating a Talkdown Directive
author: Legavy
version: 1.0.0
---

_Description: Brief description of the directive's purpose and function._

## Inputs

- **input1**: _type_ - Description of input1 (constraints if any)
- **input2**: _type_ - Description of input2 (constraints if any)

## Execution

_Description of the execution logic in natural language._

May include one of more code blocks:

```language
code_block_here
```

as well as include one or more AI prompts that should be used to generate response data:

```ai
This is a prompt for the AI to run
```

## Outputs

- **output1**: _type_ - Description of output1 (constraints if any)
- **output2**: _type_ - Description of output2 (constraints if any)

## Routing

_Description of the routing logic and conditions._

Routing might employ code to determine the next step:

```javacript
if(output1 > 1 && output2 < 10) {
  return 'Identifier'
}
```

Or might employ AI to determine the next step:

```ai
This is a prompt for the AI to run
```
