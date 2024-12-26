terraform {
  backend "s3" {
    bucket  = "poc-ecs-services"
    key     = "terraform/state/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
