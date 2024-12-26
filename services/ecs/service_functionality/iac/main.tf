# AWS module
module "aws" {
  source    = "./aws"
  region    = var.aws_region
  vpc_id    = var.aws_vpc_id
  base_name = var.aws_base_name
}
