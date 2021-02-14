#get ec2 instance data use pprint
import boto3
from pprint import pprint


aws_console_developer=boto3.session.Session(profile_name="developer")

ec2_console_resource=aws_console_developer.resource(service_name="ec2")
ec2_console_client=aws_console_developer.client(service_name="ec2")


while True:
	print("This script performs the following actions on ec2")
	print("""
		1. start
		2. stop
		3. terminate
		4. reboot
		5. Exit)
		""")

	opt=int(input("Enter your option: "))
	if opt==1:
		



response=ec2_client.describe_instances()['Reservations']

#pprint(response)
for each_item in response:
	for each in each_item['Instances']:
		print('--------------')
		print("Image ID [{}] Instance Type [{}]  Launch Time [{}]\n".format(each['ImageId'], each['InstanceType'], each['LaunchTime'].strftime("%D %H:%M")))
		print('--------------')

