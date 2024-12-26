# Create the ECR repositories
resource "aws_ecr_repository" "repo" {
  name         = "${var.base_name}_repo"
  force_delete = true
}

# Create the ECS cluster
resource "aws_ecs_cluster" "cluster" {
  name  = "${var.base_name}_cluster"
}

# Create the Task definitions
resource "aws_ecs_task_definition" "task" {
  family                   = "${var.base_name}_task"
  network_mode             = "awsvpc"
  task_role_arn            = aws_iam_role.roles["ecsTaskExecution"].arn
  execution_role_arn       = aws_iam_role.roles["ecsTaskExecution"].arn
  requires_compatibilities = ["FARGATE"]
  cpu                      = "2048"
  memory                   = "4096"
  container_definitions    = templatefile("../tasks/app.json", {
    account_id   = local.account_id
    region       = var.region
    service_name = var.base_name
  })
}
