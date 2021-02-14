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

