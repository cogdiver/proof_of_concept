#!/bin/bash
set -e

# Destroy service
./scripts/connect.sh -s iac \
    -u "terraform init && terraform destroy --target module.aws.aws_ecs_service.service --auto-approve"
