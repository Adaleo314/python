import boto3

ec2_client=boto3.client('ec2')

response=ec2_client.describe_instances()

print(len(response['Reservations']))

#############################

data=response['Reservations']

for instances in data:
    instance=instances['Instances']
    for ids in instance:
        instance_id=ids['InstanceId']
        print(instance_id)