import boto3
import random
import uuid

random_num = random.randint(1000,9999)
print(random_num)
suffix_uuid = uuid.uuid4()
print(suffix_uuid)

s3 = boto3.resource('s3')
# bucket_name = 'dct-crud-1'+str(suffix_uuid)
bucket_name = 'dct-crud-193acde8b-e03c-45fa-8604-eaf0ef21a758'

all_buckets = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_buckets:
    print(f'{bucket_name} does not exist.  Creating one now..')
    s3.create_bucket(Bucket=bucket_name)
else:
    print(f'{bucket_name} bucket already exists.  No need to create new one.')
    
# Print file1 content to console.
# with open('./aws_services_py/file_1.txt' , 'r') as file1:
#     print(file1.read())

# Upload file1 to s3 bucket
file1_location = './aws_services_py/file_1.txt'
s3.Bucket(bucket_name).upload_file(Filename= file1_location, Key='file1.txt')

# Read and print the file content.
obj = s3.Object(bucket_name,"file1.txt")
print(obj)
body = obj.get()["Body"].read()
print(type(obj.get()))
print(type(obj.get()["Body"]))
print(body)