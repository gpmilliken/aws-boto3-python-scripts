# George Milliken
# 02-15-2021
# Entered following examples in Udemy Class
# "AWS Automation of Boto3 of Python and AWS Lambda"
# https://www.udemy.com/course/aws-automation-with-boto3-of-python-and-lambda-functions/learn/lecture/14614056#overview
# No copyright claimed, no license claimed or granted
#


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
