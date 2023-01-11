import boto3

#list all ec2 instances running

ec2_client=boto3.client('ec2')

response=ec2_client.describe_instances()

print(response)