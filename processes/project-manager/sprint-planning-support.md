---
title: sprint-planning-support
---

### Talkdown Directives for Sprint Planning Support

1. **Backlog Pre-filling**
   - `RetrieveBacklogTemplate()` - Obtain a template or previous sprint backlog items for reference.
   - `CreateTaskInBacklog(taskDetails)` - Create new tasks in the backlog based on input or template.
   - `UpdateTaskInBacklog(taskId, taskDetails)` - Update existing tasks with new details.

2. **Estimation Assistance**
   - `RetrieveEstimationGuidelines()` - Get the estimation guidelines or standards.
   - `SuggestEffortEstimation(taskDetails)` - Provide a suggested effort estimation for a task based on similar completed tasks, using historical data.
   - `RequestEstimationConfirmation(estimation, taskId)` - Request confirmation or adjustment of suggested effort estimations from the development team.

3. **Sprint Goals and Objectives Setup**
   - `QueryActiveSprintGoals()` - Check for goals that are set for the current or upcoming sprint.
   - `SetSprintGoal(sprintId, goalDetails)` - Define and set a sprint goal in Azure Boards for the sprint.
   - `LinkTasksToGoal(sprintGoalId, tasks)` - Associate tasks from the backlog with the sprint goal.
   - `GenerateSprintObjectiveDocument(sprintGoal)` - Create a document detailing the sprint goals and objectives.

### Sequence of Operations for Sprint Planning Support

1. **Initiating Backlog Pre-filling**
   - Call `RetrieveBacklogTemplate()` to get the list of tasks commonly added to new sprints, if applicable.
   - For each task that needs to be pre-filled in the backlog:
     - Call `CreateTaskInBacklog(taskDetails)` with the necessary details for the backlog item.

2. **Facilitating Estimation Process**
   - Call `RetrieveEstimationGuidelines()` to ensure estimations follow team practices.
   - For each new or updated backlog item:
     - Call `SuggestEffortEstimation(taskDetails)` to generate a proposed estimation based on AI analysis.
     - Call `RequestEstimationConfirmation(estimation, taskId)` to push the estimation proposal to the team for confirmation or discussion.

3. **Setting Up Sprint Goals and Objectives**
   - Call `QueryActiveSprintGoals()` to determine if sprint goals for the upcoming sprint have already been defined.
   - If sprint goals need to be set:
     - Call `SetSprintGoal(sprintId, goalDetails)` to define each goal or objective.
     - Call `LinkTasksToGoal(sprintGoalId, tasks)` to map the backlog tasks to the defined sprint goals.
   - Call `GenerateSprintObjectiveDocument(sprintGoal)` to produce a formal sprint goal document that can be distributed and discussed among the team.

Specifically, Azure DevOps API endpoints would be targeted by the directives, which would wrap the API calls in a layer of business logic provided by the AI's understanding of project management and agile processes. The AI system would use the directives in various combinations and sequences depending on the context and requirements of the sprint planning meeting, ensuring the process aligns with agile principles and team practices.
