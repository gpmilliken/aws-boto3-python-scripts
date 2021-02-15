# George Milliken
# 02-15-2021
# Entered following examples in Udemy Class
# "AWS Automation of Boto3 of Python and AWS Lambda"
# https://www.udemy.com/course/aws-automation-with-boto3-of-python-and-lambda-functions/learn/lecture/14614056#overview
# No copyright claimed, no license claimed or granted
#
#get ec2 instance data use pprint

import boto3
from pprint import pprint


aws_console_developer=boto3.session.Session(profile_name="developer")

ec2_client=aws_console_developer.client(service_name="ec2")

response=ec2_client.describe_instances()['Reservations']

pprint(response)
for each_item in response:
	for each in each_item['Instances']:
		print('--------------')
		print("Image ID [{}] Instance Type [{}]  Launch Time [{}]\n".format(each['ImageId'], each['InstanceType'], each['LaunchTime'].strftime("%D %H:%M")))
		print('--------------')

