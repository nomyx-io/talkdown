# Project Quality Management

## Overview

The virtual project manager (VPM) will manage the project quality. This includes setting quality standards, conducting quality assurance, and performing quality control.

## Key Features

1. **Quality Planning**
   - `SetQualityStandards(standards)` - Set the quality standards for the project.
   - `UpdateQualityStandards(standards)` - Update the quality standards.
2. **Quality Assurance and Control**
   - `ConductQualityAssurance(activityId)` - Conduct quality assurance for a specific activity.
   - `PerformQualityControl(activityId)` - Perform quality control for a specific activity.

### Sequence of Operations for Project Quality Management

1. **Planning Quality**
   - At the start of the project, execute `SetQualityStandards(standards)` to set the quality standards.
   - Use `UpdateQualityStandards(standards)` to update the quality standards when necessary.
2. **Assuring and Controlling Quality**
   - For each project activity:
     - Use `ConductQualityAssurance(activityId)` to conduct quality assurance.
     - Call `PerformQualityControl(activityId)` to perform quality control.
