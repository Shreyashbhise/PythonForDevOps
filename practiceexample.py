# Autoscaling Script for AWS EC2 Instances

import boto3

# Replace with your AWS access key and secret key
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Update with your AWS region
cpu_threshold_high = 80
cpu_threshold_low = 30

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Function to get CPU utilization of EC2 instances
def get_cpu_utilization(instance_id):
    # Simulated function for getting CPU utilization
    # Replace with actual AWS CloudWatch or monitoring data retrieval
    return 60  # Replace with real CPU utilization

# Function to adjust the number of instances based on CPU utilization
def autoscale_instances():
    instances = ['instance_id_1', 'instance_id_2']  # Replace with your instance IDs
    for instance_id in instances:
        cpu_utilization = get_cpu_utilization(instance_id)
        if cpu_utilization > cpu_threshold_high:
            # Scale up by launching new instances
            # Implement the logic to create new instances here
            print("Scaling up instance {}".format(instance_id))
        elif cpu_utilization < cpu_threshold_low:
            # Scale down by terminating instances
            # Implement the logic to terminate instances here
            print("Scaling down instance {}".format(instance_id))

# Continuous monitoring and scaling loop
while True:
    autoscale_instances()
    # Add a delay or sleep for a specific interval before checking again

