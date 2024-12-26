# Specify the required version of Terraform
terraform {
  required_version = ">= 1.0.0" # 1.8.5

  # Specify the required providers and their versions
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0" # 5.52.0
    }
  }
}
