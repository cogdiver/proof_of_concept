#!/bin/bash

# -------------------------------------------------------------------------------------
# Script to automate the setup of a Google Cloud Platform (GCP) project configuration.
# -------------------------------------------------------------------------------------

# set login
./scripts/gcp_login.sh

# Set environment variables using the .env file
source .env

# Create bigquery dataset
bq mk -f $PROJECT:poc

# Init database
find database/init/ \
  -type f \
  -name "*.sql" \
  -exec sed 's/<PROJECT>/'$PROJECT'/g' {} \; | bq query --nouse_legacy_sql
