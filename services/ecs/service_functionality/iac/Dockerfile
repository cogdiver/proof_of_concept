# Use the official Terraform image from HashiCorp
FROM hashicorp/terraform:1.8.5

# Copy files from the host to the container
COPY ./tasks /app/tasks
COPY ./scripts /app/scripts
COPY ./iac /app/iac

# Set the working directory inside the container
WORKDIR /app/iac

# Define the entry point for the container
ENTRYPOINT ["terraform"]

# Define the default command
CMD ["plan"]
