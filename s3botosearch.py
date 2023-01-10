import boto3

resource = boto3.client('s3')

#list # of buckets
#see all buckets in s3
for bucket in resource.buckets.all():
    print(bucket.name)

#listing creation date of buckets


bucket in resource(['Buckets']):
    print(bucket[Name])