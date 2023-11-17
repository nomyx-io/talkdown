# Project Dependencies

## Overview

The virtual project manager (VPM) will manage the dependencies within the project. This includes maintaining a list of all project dependencies and tracking their current progress.

## Key Features

1. **Dependency Tracking**
   - `TrackDependency(dependencyId)` - Monitor the progress of a specific project dependency.
   - `UpdateDependencyStatus(dependencyId, status)` - Update the status of a specific project dependency.
2. **Dependency Notification**
   - `SendDependencyNotification(recipient(s), message)` - Send a notification to one or more recipients about a dependency status update.
   - `SubscribeToDependencyUpdates(dependencyId)` - Enable automatic updates to specified dependencies.
   - `ConfigureDependencyNotificationSettings(settings)` - Adjust the dependency notification preferences and triggers within Azure Boards.

### Sequence of Operations for Project Dependency Management

1. **Tracking Dependencies**
   - Continuously execute `TrackDependency(dependencyId)` to monitor the progress of each project dependency.
   - Upon detection of a status change, call `UpdateDependencyStatus(dependencyId, status)` to update the dependency status in Azure Boards.
2. **Sending and Managing Dependency Notifications**
   - For each status update:
     - Use `SubscribeToDependencyUpdates(dependencyId)` to enable automatic notifications.
     - Call `SendDependencyNotification(recipient(s), message)` to inform the relevant stakeholders about the dependency status update.
   - Use `ConfigureDependencyNotificationSettings(settings)` to ensure notifications are being sent according to user preferences.
