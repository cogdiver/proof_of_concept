# FastAPI Long Running Operations PoC

## Setup Instructions
This document provides a brief guide on how to get the FastAPI Proof of Concept (PoC) for long-running operations up and running on your local machine.


1. **Prerequisites:** Before you begin, ensure you have [Docker](https://www.docker.com/products/docker-desktop) installed.

2. **Initialize the environment:** Run the `scripts/setup.sh` script to build and start the Docker container. This script takes care of setting up everything needed for the PoC.

3. **Accessing the Application:** Once the setup script completes, the FastAPI server will be running inside a Docker container. You can access the FastAPI documentation and try out the endpoints by navigating to: http://localhost:8000/docs.
>This interface provides a user-friendly way to interact with the API and understand the functionalities of the long-running operations.

4. **Detailed Documentation:** For detailed information on the proof of concept, its execution, and findings, please consult the documentation provided in the [DOCUMENTATION.md](DOCUMENTATION.md) file.

5. **Cleaning**: Run the `scripts/cleanup.sh` script to delete volumes and containers instantiated with docker.
