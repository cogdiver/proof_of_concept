# ECS Services Functionality PoC

## Setup Instructions

Before running any tests or scripts, please follow these setup steps:

1. **Environment Configuration**:
   - Create a `.env` file based on the `.env.sample` provided in this repository.
   - Ensure you add your AWS credentials including `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION` to the `conn/.aws` file. These credentials are essential for accessing ECS and related AWS services.

2. **Initialization**:
   - Run the `scripts/setup.sh` script to install necessary dependencies such as `awscli` and `jq`.
   - Execute the `scripts/deploy.sh up` script to initialize the ECS cluster and register the required task definitions for this proof of concept.

3. **Documentation**: For detailed information on this proof of concept, its goals, and execution, please consult the documentation provided in the [Analysis of the poc](DOCUMENTATION.md).

4. **Cleaning**:
   - Run the `scripts/deploy.sh down` script to remove all deployed ECS services and tasks.
   - Execute the `scripts/cleanup.sh` script to clean up the local environment by removing any containers or images that were created.

Following these steps will ensure you have all necessary configurations and resources to explore the functionality of services in ECS.
