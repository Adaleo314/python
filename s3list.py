import boto3

#list items in s3 bucket

s3_resource = boto3.resource('s3')

s3_resource.list_objects(Bucket='mybucket')['Contents']


if len(objects) > 0:
    print('object exists')
    
    
for object in objects:
    print(object)
