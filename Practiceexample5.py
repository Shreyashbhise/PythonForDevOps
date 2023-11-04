# Automating Backup and Restore script using python

import boto3
import os
import shutil

# Replace these with your AWS access key and secret key
aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
aws_region = 'us-east-1'  # Update with your AWS region
s3_bucket_name = 'your-s3-bucket-name'

# Source directory to be backed up
source_directory = '/path/to/source_directory'

# Destination directory for the backup
backup_directory = '/path/to/backup_directory'

# Backup: Copy the contents of the source directory to the backup directory
shutil.copytree(source_directory, backup_directory)
print("Backup completed successfully. Files copied to: {}".format(backup_directory))

# Restore: Copy the contents from the backup directory to the source directory
shutil.rmtree(source_directory)
shutil.copytree(backup_directory, source_directory)
print("Restored backup to {}".format(source_directory))

# Initialize the Boto3 S3 client
s3 = boto3.client('s3', region_name=aws_region, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

# Upload the backup to an S3 bucket
s3.upload_file(backup_directory, s3_bucket_name, 'backup.zip')
print("Backup uploaded to S3 bucket: {}".format(s3_bucket_name))
