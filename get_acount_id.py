# Get Account ID three different ways

import boto3

aws_console_developer=boto3.session.Session(profile_name="developer")

sts_console=aws_console_developer.client(service_name="sts")

print('----------')
print(sts_console.get_caller_identity().get('Account'))
print('----------')


print('----------')
response=sts_console.get_caller_identity()
print(response['Account'])
print('----------')


print('----------')
response=sts_console.get_caller_identity()
print(response.get('Account'))
print('----------')
