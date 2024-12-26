######################################
### AWS Variables
######################################
# AWS Provider Variables
variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
}

# Network Variables
variable "aws_vpc_id" {
  description = "The VPC ID where the RDS instance will be deployed"
  type        = string
}

# General Variables
variable "aws_base_name" {
  description = "The base name of the project"
  type        = string
}
