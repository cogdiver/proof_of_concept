# AWS Provider Configuration
provider "aws" {
  region = var.region
}

# Get account data
data "aws_caller_identity" "current" {}
