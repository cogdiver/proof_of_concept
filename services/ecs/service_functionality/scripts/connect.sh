#!/bin/bash

################################################
# Script for Starting and Entering Local Docker Containers
#
# This script starts a specified Docker service
# using Docker Compose and then opens an interactive
# shell session in the running container.
################################################

# Function to display help menu
Usage() {
    echo "Usage: $0 [OPTIONS] [-s SERVICE] [-u USE_SHELL]"
    echo
    echo "Options:"
    echo "  -h|-help    Show this help message and exit"
    echo
    echo "Parameters:"
    echo "  SERVICE       Service to start and enter"
    echo "  USE_SHELL     Shell to use (default: current user shell)"
    echo
    echo -e "[NOTE] If no USE_SHELL is provided, the script will use the current user shell."
    echo
    echo " Example:"
    echo "     $0 -s app"
    echo "     $0 -s app -u sh"
    echo "     $0 -s app -u python"
}

# Function to start service and enter the shell
StartAndEnterService() {
    # Start the service using Docker Compose and enter the shell
    docker compose up poc-$SERVICE -d
    docker exec -it poc-$SERVICE sh -c "$USE_SHELL"
}

# Define default variables
SERVICE=""
USE_SHELL=$SHELL

# Parse named parameters
while getopts "s:u:h" opt; do
    case ${opt} in
        s ) SERVICE=$OPTARG ;;
        u ) USE_SHELL=$OPTARG ;;
        h ) Usage; exit 0 ;;
        \? ) echo '[Invalid parameter]'; Usage; exit 1 ;;
    esac
done

# Check if SERVICE is provided
if [ -z "$SERVICE" ]; then
    echo "[Error] -s SERVICE is required."
    Usage
    exit 1
fi

# Build de imange and enter the container's shell
StartAndEnterService
