# Generate Data Model

Given a description of a project, task, process, or data, this directive generates a data model to properly represent the project, task, process, or data.

## Input

- `description` (Required): A description of the project, task, process, or data.
- `model_type` (Optional): The type of model to generate. Default is "ER". Other options are "UML", "BPMN", etc.

## Execution

1. Parse the description to identify the key elements that need to be modelled. These might be entities, processes, data points, etc.
2. Based on the model_type, generate the appropriate model. This could involve creating an Entity-Relationship diagram for a database, a UML diagram for software architecture, or a BPMN diagram for a business process.
3. Ensure that the model accurately represents all elements identified in the description.

## Output

- `data_model`: The generated data model. This could be a diagram, text-based representation, or other form depending on the model_type.
