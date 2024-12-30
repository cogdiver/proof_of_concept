# ECS Scheduled Tasks PoC

## Setup Instructions

Before running any tests or scripts, please follow these setup steps:

1. **Environment Configuration**:
   - Create a `.env` file based on the `.env.sample` provided in this repository.
   - Ensure you add your AWS credentials including `ACCESS_KEY`, `SECRET_KEY`, and `REGION` to the `.env` file. These credentials are essential for accessing ECS and related AWS services.

2. **Initialization**:
   - Run the `scripts/setup_scheduled_tasks.sh` script to configure the ECS cluster and schedule tasks using Amazon EventBridge.

3. **Execution**:
   - Use the `scripts/run_scheduled_tasks.sh` script to trigger and test the scheduled tasks. This will allow you to validate the integration of ECS with EventBridge for task scheduling.

4. **Documentation**:
   - For detailed information on this proof of concept, its goals, and execution, please consult the documentation provided in the [Analysis of the poc](DOCUMENTATION.md).

5. **Cleaning**:
   - Run the `scripts/cleanup_scheduled_tasks.sh` script to delete the ECS cluster, EventBridge rules, and any other associated resources.

Following these steps will ensure you have all necessary configurations and resources to explore task scheduling in ECS.
