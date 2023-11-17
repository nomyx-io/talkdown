# Generate HTML Layout for User Interface

Given a user interface description - list of user interface fields and actions - this directive will generate the optimal layout for the field. It will return HTML with inline styling that lays out the user interface fields.

## Input

- `uiDescription` (Required): An array of UI fields and actions descriptions. Each description should have the following properties:
  - `type`: The type of the UI field (e.g., "text", "button", etc.)
  - `label`: The label for the UI element
  - `action`: An optional action associated with the UI element

## Execution

1. Parse the `uiDescription` input to understand the kind of fields and actions described.
2. For each UI element described, generate the appropriate HTML tag(s). These should include necessary attributes such as `id`, `class`, and `style`.
   - The style should be inline, assigning appropriate values to CSS properties such as `width`, `height`, `margin`, and `padding` to ensure optimal layouting.
   - The placement of each UI element should be determined such that it provides an enjoyable and practical user experience.
3. Combine all generated HTML tags into a single string of HTML code, ensuring that they are structured in a way that maintains the order and relationships described in the input.

## Output

- `html` (Required): The generated HTML code. This should contain all UI elements described in the input, laid out optimally using inline styles.

## Examples

__Input:__

`[{"type": "text", "label": "First Name"}, {"type": "text", "label": "Last Name"}, {"type": "button", "label": "Submit", "action": "submitForm"}]`

__Output:__

`<div><label for='first-name'>First Name</label><input id='first-name' type='text' style='width: 100%; margin: 5px 0;'></div><div><label for='last-name'>Last Name</label><input id='last-name' type='text' style='width: 100%; margin: 5px 0;'></div><div><button id='submit' style='width: 100%; margin-top: 10px;' onclick='submitForm()'>Submit</button></div>`
