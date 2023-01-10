import boto3
import os
import glob

s3_resource = boto3.client('s3')

#how to upload single file to s3
    
s3_resource.upload_file(
    Filename='test.txt',
    Bucket='mybucket-boto3',
    Key='test.txt')
    
    

