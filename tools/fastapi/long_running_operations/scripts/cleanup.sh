#!/bin/bash

# ------------------------------------------------------------------------
# This script automates the cleanup of services created during the setup.
# ------------------------------------------------------------------------

docker compose down --volumes --remove-orphans
