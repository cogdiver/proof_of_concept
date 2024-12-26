locals {
  account_id = data.aws_caller_identity.current.account_id
  # Components that will use IAM roles and policies
  iam_components = {
    "ecsTaskExecution" = {
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
