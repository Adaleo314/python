import boto3

s3_resource = boto3.client('s3')

s3_resource.delete_object(Bucket='adaleo314bucket', Key='qomk9yntlnq41.webp')


import os
import glob

s3_resource.list_objects(Bucket='adaleo314bucket')["Contents"]


for object in objects:
    print(object['Key'])
    