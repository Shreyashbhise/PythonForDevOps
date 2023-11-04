# Automating AWS Instance Termination script using python

import boto3

# Replace these with your AWS access key and secret key
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Update with your AWS region

# Initialize the Boto3 EC2 client
ec2 = boto3.client('ec2', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Define the tag criteria for instance termination
tag_filter = [{'Name': 'tag:Environment', 'Values': ['Development']},
              {'Name': 'tag:AutoTerminate', 'Values': ['True']}]

# List instances based on the tag criteria
response = ec2.describe_instances(Filters=tag_filter)

# Terminate instances that match the criteria
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        ec2.terminate_instances(InstanceIds=[instance_id])
        print("Terminated instance {}".format(instance_id))
