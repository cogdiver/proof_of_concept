#!/bin/bash

# ------------------------------------------------------------------------
# This script automates the cleanup of services created during the setup.
# ------------------------------------------------------------------------

# set login
./scripts/gcp_login.sh

# Set environment variables using the .env file
source .env

# Down database
find database/down/ \
  -type f \
  -name "*.sql" \
  -exec sed 's/<PROJECT>/'$PROJECT'/g' {} \; | bq query --nouse_legacy_sql

# Delete dataset if empty
bq rm -f $PROJECT:poc
