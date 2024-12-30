locals {
  account_id = data.aws_caller_identity.default.account_id
  base_name_with_hyphen = replace(var.base_name, "_", "-")

  # Components that will use IAM roles and policies
  iam_components = {
    "ecsServiceExecution" = {
      "service": "ecs-tasks.amazonaws.com",
      "policy_statement": [
        {
          "Effect": "Allow",
          "Action": [
            "logs:*",
            "cloudwatch:GenerateQuery"
          ],
          "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
            ],
            "Resource": "*"
        }
      ]
    }
  }
}
