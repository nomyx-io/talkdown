# Validate Result Directive

This directive validates the given task result against the given result reference. It checks for quality equivalence and whether the task result contains the appropriate level of detail. The directive returns a list of remaining tasks to be performed on the item if validity is denied or an empty list if the task result is validated.

## Input

The directive requires the following inputs:

* `task_result` - The result of the task to be validated.
* `result_reference` - The reference against which the task result will be validated.

## Execution

1. Compare the `task_result` with the `result_reference` for equivalence in quality and detail.
2. If the `task_result` does not match the `result_reference`, identify the list of remaining tasks to be performed. This is done by examining the differences between the two.
3. If the `task_result` matches the `result_reference`, the task is considered complete and thus, no further actions are required.

## Output

This directive will output the following:

* `validation_status` - The status of the validation, `True` for validated and `False` for unvalidated.
* `remaining_tasks` - An array of strings, containing the list of remaining tasks to be performed. This array is empty if the task result is validated.

## Examples

To illustrate how the directive works, considering the following example:

__Input:__

* `task_result` = "Complete report on sales strategy".
* `result_reference` = "Complete report on sales strategy including forecast, current market trends, and SWOT analysis".

__Output:__

* `validation_status` = False
* `remaining_tasks` = ['Include forecast', 'Include current market trends', 'Include SWOT analysis']
