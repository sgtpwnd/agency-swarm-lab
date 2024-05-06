#!/bin/bash

# Function to log errors and exit
log_error() {
  echo "Error: $1" >&2
  exit 1
}

# Step 1: Pull the latest RabbitMQ image with management plugins
echo "Pulling the latest RabbitMQ Docker image with management plugins..."
docker pull rabbitmq:management || log_error "Failed to pull RabbitMQ Docker image."

# Step 2: Run the RabbitMQ container with custom settings
echo "Starting RabbitMQ container with custom user, password, exposed ports, and data persistence..."
docker run -d \
  --name myrabbitmq \
  -e RABBITMQ_DEFAULT_USER=myuser \
  -e RABBITMQ_DEFAULT_PASS=mypassword \
  -p 5672:5672 \
  -p 15672:15672 \
  -v myrabbitmq_data:/var/lib/rabbitmq \
  rabbitmq:management || log_error "Failed to start RabbitMQ container."

echo "RabbitMQ container is now running with management plugins."
echo "Access the management UI at http://localhost:15672"

# Note: Replace 'myuser' and 'mypassword' with your desired username and password.
# Ports 5672 and 15672 are exposed for RabbitMQ server and management UI respectively.
# Data is persisted in the volume 'myrabbitmq_data'.