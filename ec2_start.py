import boto3

resource = boto3.resource('ec2')

#starting 3 instances for purpose of project
#ami is Amazon Linux, left out SSH key 
instances = resource.create_instances(
    ImageId='ami-0b5eea76982371e91',
    MinCount=3,
    MaxCount=3,
    InstanceType='t2.micro',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'Test Instances'},
            {'Key': 'Environment', 'Value': 'Dev'}] 
                },
            ],
            )
            
for i in instances[]:
    print('Created Instance ID: '())
####
    