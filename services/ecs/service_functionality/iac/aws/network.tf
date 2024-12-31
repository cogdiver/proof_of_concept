# Create a Security Group for the ECS execution
resource "aws_security_group" "sg" {
  name        = "${var.base_name}_sg"
  description = "Security group for ECS service execution"
  vpc_id      = var.vpc_id

  # Allow inbound traffic to ECS
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust as necessary for security
  }

  # Allow outbound traffic to ECR
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust as necessary for security
  }
}

# Create a Security Group for the LB
resource "aws_security_group" "lb_sg" {
  name        = "${var.base_name}_lb_sg"
  description = "Security group for the Load Balancer"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Adjust as necessary for security
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Adjust as necessary for security
  }
}

# Create a load balancer for the ECS service
resource "aws_lb" "lb" {
  name               = "${local.base_name_with_hyphen}-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = data.aws_subnets.default.ids

  enable_deletion_protection = false
}

# Create a target group for the ECS service
resource "aws_lb_target_group" "tg" {
  name     = "${local.base_name_with_hyphen}-tg"
  port     = 8080
  protocol = "HTTP"
  vpc_id   = var.vpc_id
  target_type = "ip"

  health_check {
    path                = "/health"
    interval            = 60
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
    matcher             = "200"
  }

  lifecycle {
    prevent_destroy = false
  }
}

# Create a listener for the load balancer
resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_lb.lb.arn
  port              = 8080
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.tg.arn
  }

  lifecycle {
    prevent_destroy = false
  }
}
