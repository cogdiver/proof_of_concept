# AWS Provider Configuration
provider "aws" {
  region = var.region
}

# Get account data
data "aws_caller_identity" "default" {}

# Get default VPC subnets
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}
