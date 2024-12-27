#!/bin/bash

#####################################
# This script deploys and tears down services on AWS ECS.
# It uses Terraform to manage infrastructure and Docker to build and push images.
# Main functions:
# - Up: Brings up the services, creates an S3 bucket, deploys infrastructure with Terraform,
#       builds and pushes a Docker image to ECR, and creates an ECS service.
# - Down: Tears down the services and destroys the infrastructure with Terraform.
########################################

# Function to display usage
Usage() {
    echo "Usage: $0 {up|down}"
    exit 1
}

set -a; . ./conn/aws; set +a # Load aws credentials
. .env # Load general environment variables


# Function to bring services up
Up() {
    echo "Bringing services up..."
    REGION=$AWS_DEFAULT_REGION
    SERVICE=$TF_VAR_aws_base_name
    VPC_ID=$TF_VAR_aws_vpc_id

    AWS_ACCOUNT_ID=`aws sts get-caller-identity --query Account --output text`

    # Create a bucket for the Terraform backend before deploying IaC
    BUCKET_NAME=$(echo $SERVICE | tr '_' '-')
    aws s3api head-bucket --bucket $BUCKET_NAME --region $REGION > /dev/null 2>&1

    if [ $? -ne 0 ]; then
        aws s3api create-bucket --bucket $BUCKET_NAME --region $REGION
    fi

    # Deploy Infrastructure
    ./scripts/connect.sh -s iac -u "terraform init && terraform apply --auto-approve"

    # Log in to ECR
    aws ecr get-login-password \
        --region $REGION | \
    docker login \
        --username AWS \
        --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

    # Build and tag the Docker image
    docker build \
        -f ./app/Dockerfile \
        -t $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/${SERVICE}_repo:latest \
        app

    # Push Docker image to AWS
    docker push $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/${SERVICE}_repo:latest

    # Get security group id
    SG_ID=$(aws ec2 describe-security-groups \
        --group-name ${SERVICE}_sg \
        --query SecurityGroups[0].GroupId \
        --output text)

    # Get Subnetworks
    SUBNETS=$(aws ec2 describe-subnets \
        --filters "Name=vpc-id,Values=$VPC_ID" \
        --query "Subnets[].SubnetId" \
        --output text \
        --output json | jq -r 'join(",")')

    # Run the ECS service
    SERVICE_ARN=`aws ecs create-service \
        --cluster ${SERVICE}_cluster \
        --service-name ${SERVICE}_app \
        --task-definition ${SERVICE}_task \
        --desired-count 1 \
        --launch-type FARGATE \
        --network-configuration "awsvpcConfiguration={subnets=[$SUBNETS],securityGroups=[$SG_ID],assignPublicIp=ENABLED}" \
        --region $REGION \
        --query "service.serviceArn" \
        --output text`

    # Save Tasks ARN
    echo $SERVICE_ARN >> tmp/.services
}

# Function to bring services down
Down() {
    echo "Bringing services down..."

    # Destroy Infrastructure
    ./scripts/connect.sh -s iac -u "terraform init && terraform destroy --auto-approve"
}

# Main script logic
case "$1" in
    up) Up ;;
    down) Down ;;
    *) Usage ;;
esac
