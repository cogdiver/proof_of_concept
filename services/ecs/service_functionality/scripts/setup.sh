#!/bin/bash

# Function to install AWS CLI
AWSInstall() {
  # Install unzip package
  apt-get install -y unzip

  # Download the AWS CLI version 2 for Linux (64-bit)
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

  # Unzip the downloaded AWS CLI package
  unzip awscliv2.zip

  # Run the AWS CLI installation script
  ./aws/install
}

# Install AWS CLI if it is not installed
command -v aws || AWSInstall
