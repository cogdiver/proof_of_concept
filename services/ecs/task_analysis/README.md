# ECS Tasks Analysis PoC

## Setup Instructions

Before running any tests or scripts, please follow these setup steps:

1. **Environment Configuration**:
   - Create a `.env` file based on the `.env.sample` provided in this repository.
   - Ensure you add your AWS credentials including `ACCESS_KEY`, `SECRET_KEY`, and `REGION` to the `.env` file. These credentials are essential for accessing ECS and related AWS services.

2. **Initialization**:
   - Run the `scripts/setup_tasks.sh` script to initialize the ECS cluster and register the required task definitions for this proof of concept.

3. **Execution**:
   - Use the `scripts/run_tasks.sh` script to run tasks in the ECS cluster. This script will allow you to analyze the behavior, resource usage, and performance of the tasks.

4. **Documentation**:
   - For detailed information on this proof of concept, its goals, and execution, please consult the documentation provided in the [Analysis of the poc](DOCUMENTATION.md).

5. **Cleaning**:
   - Run the `scripts/cleanup_tasks.sh` script to delete the ECS cluster, task definitions, and any other associated resources.

Following these steps will ensure you have all necessary configurations and resources to explore task analysis in ECS.
