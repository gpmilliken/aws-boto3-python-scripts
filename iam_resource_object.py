# George Milliken
# 02-15-2021
# Entered following examples in Udemy Class
# "AWS Automation of Boto3 of Python and AWS Lambda"
# https://www.udemy.com/course/aws-automation-with-boto3-of-python-and-lambda-functions/learn/lecture/14614056#overview
# No copyright claimed, no license claimed or granted
#


iam_con_cli=aws_mag_con.resource(service_name="iam")
ec2_con_cli=aws_mag_con.resource(service_name="ec2")
s3_con_cli=aws_mag_con.resource(service_name="s3")

# this results in 
# iam.ServiceResource()
print(iam_con_cli)

print(dir(ec2_con_cli.instances.__hash__()))
print('---------------')
print(ec2_con_cli.instances.__hash__())
print('---------------')

for each_item in ec2_con_cli.instances.all():
	print(each_item)

	
