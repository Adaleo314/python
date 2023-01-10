import boto3

resource = boto3.resource('s3')

#list # of buckets 
bucket_list = list(resource.buckets.all())
len(bucket_list)

#see all buckets in s3
for bucket in resource.buckets.all():
    print(bucket.name)

