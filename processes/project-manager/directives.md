---
title: directives
---
1. **Task Management Directives**
    - `CreateTask(item, attributes)` - Create a new work item with specified attributes.
    - `UpdateTask(item, attributes)` - Update an existing work item with new attributes.
    - `CloseTask(item)` - Close a specified work item.
    - `PrioritizeTasks(list)` - Order a list of tasks by priority.
    - `QueryTasks(query)` - Retrieve work items based on a query.

2. **Communication Directives**
    - `SendEmail(recipient, subject, body)` - Compose and send an email.
    - `PostMessage(channel, message)` - Post a message to a Teams channel or chat.
    - `ScheduleMeeting(participants, topic, startTime)` - Schedule a meeting in Teams.
    - `GenerateSummary(topic, items)` - Generate a summary report of specified items or meetings.
    - `NotifyUser(user, notification)` - Send a notification to an individual user.

3. **Reporting Directives**
    - `CreateReport(data, type)` - Generate a specific type of report based on provided data.
    - `DistributeReport(report, recipients)` - Send a generated report to a list of recipients.
    - `UpdateDashboard(dashboard, data)` - Refresh a dashboard with the latest data.

4. **Data Processing and Analysis Directives**
    - `ExtractData(source, parameters)` - Extract data from a source using provided parameters.
    - `TransformData(data, transformation)` - Apply a transformation to data (e.g., calculate burndown data).
    - `AnalyzeData(data, analysisType)` - Perform a specified type of analysis on the data.

5. **Automation and Workflow Directives**
    - `CreateAutomationRule(trigger, action)` - Create an automation rule with specified trigger and action.
    - `RunWorkflow(sequence)` - Execute a predefined sequence of operations.
    - `UpdateWorkflow(workflow, changes)` - Make updates to an existing workflow.

6. **Meeting Facilitation and Record-Keeping Directives**
    - `RecordMeeting(meetingID)` - Record the audio or video for a meeting.
    - `TranscribeMeeting(meetingID)` - Generate a text transcription of a meeting recording.
    - `AnalyzeDiscussion(topic, transcript)` - Analyze a meeting transcript for specific discussion points.
    - `FollowUp(actionItems)` - Assign and track follow-up items post-meeting.

7. **User Interaction Directives**
    - `RequestInput(requestType, prompt)` - Ask for user input based on the request type and prompt.
    - `ValidateInput(input, rules)` - Validate user input according to specified rules.
    - `GuideUserThroughProcess(user, process)` - Assist a user through a predefined process.

8. **Integration and Collaboration Directives**
    - `LinkItems(item1, item2)` - Create a link between two work items, signifying a dependency or relationship.
    - `SyncService(service1, service2, data)` - Synchronize data between two different services.
    - `DelegateTask(task, user)` - Assign a task to a user with delegation rules.

9. **Compliance and Governance Directives**
    - `AuditChanges(timeFrame)` - Review changes within a specified time frame for auditing purposes.
    - `EnforcePolicies(policyList, item)` - Ensure that a work item meets the specified list of policies.
    - `LogActivity(activity, metadata)` - Record an activity with its associated metadata for compliance tracking.

10. **Resource Management Directives**
    - `AllocateResources(task, resources)` - Assign resources to a task.
    - `ForecastResources(timeFrame)` - Project resource usage and needs over a given time frame.
    - `OptimizeResourceAllocation(project)` - Suggest the most efficient resource allocation for a project.
