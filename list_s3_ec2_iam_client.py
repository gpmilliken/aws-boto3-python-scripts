# George Milliken
# 02-15-2021
# Entered following examples in Udemy Class
# "AWS Automation of Boto3 of Python and AWS Lambda"
# https://www.udemy.com/course/aws-automation-with-boto3-of-python-and-lambda-functions/learn/lecture/14614056#overview
# No copyright claimed, no license claimed or granted
#
# uses client access
#

import boto3

aws_mag_con=boto3.session.Session(profile_name="developer")

iam_con_cli=aws_mag_con.client(service_name="iam")
ec2_con_cli=aws_mag_con.client(service_name="ec2")
s3_con_cli=aws_mag_con.client(service_name="s3")

# List all iam users using client object
response = iam_con_cli.list_users()

for each_user in response['Users']:
	print(each_user['UserName'])

ec2_response=ec2_con_cli.describe_instances()

#print(ec2_response)

for each_instance in ec2_response['Reservations']:
	for each_item in each_instance['Instances']:
		print('---------')
		print(each_item['InstanceId'])
		print('---------')

s3_response=s3_con_cli.list_buckets()

for s3_bucket in s3_response['Buckets']:
	print('*************')
	print(s3_bucket['Name'])
	print('*************')

