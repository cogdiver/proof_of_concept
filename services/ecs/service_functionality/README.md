# ECS Services Functionality PoC

## Setup Instructions

Before running any tests or scripts, please follow these setup steps:

1. **Environment Configuration**:
   - Create a `.env` file based on the `.env.sample` provided in this repository.
   - Ensure you add your AWS credentials including `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION` to the `conn/.aws` file. These credentials are essential for accessing ECS and related AWS services.

2. **Initialization**: Run the `scripts/setup_tasks.sh` script to initialize the ECS cluster and register the required task definitions for this proof of concept.

3. **Documentation**: For detailed information on this proof of concept, its goals, and execution, please consult the documentation provided in the [Analysis of the poc](DOCUMENTATION.md).

4. **Cleaning**: Run the `scripts/cleanup.sh` script to delete the ECS cluster, services, and any other associated resources.

Following these steps will ensure you have all necessary configurations and resources to explore the functionality of services in ECS.
