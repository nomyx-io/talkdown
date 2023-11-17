# Project Procurement Management

## Overview

The virtual project manager (VPM) will manage the project procurement. This includes planning procurement, conducting procurement, and controlling procurement.

## Key Features

1. **Procurement Planning**
   - `PlanProcurement(procurementDetails)` - Plan the procurement details for the project.
   - `UpdateProcurementPlan(procurementDetails)` - Update the procurement plan.
2. **Conducting and Controlling Procurement**
   - `ConductProcurement(procurementId)` - Conduct procurement for a specific item.
   - `ControlProcurement(procurementId, controlDetails)` - Control the procurement process for a specific item.

### Sequence of Operations for Project Procurement Management

1. **Planning Procurement**
   - At the start of the project, execute `PlanProcurement(procurementDetails)` to plan the procurement details.
   - Use `UpdateProcurementPlan(procurementDetails)` to update the procurement plan when necessary.
2. **Conducting and Controlling Procurement**
   - For each procurement item:
     - Use `ConductProcurement(procurementId)` to conduct the procurement.
     - Call `ControlProcurement(procurementId, controlDetails)` to control the procurement process.
