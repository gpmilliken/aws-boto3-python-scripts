# George Milliken
# 02-15-2021
# Entered following examples in Udemy Class
# "AWS Automation of Boto3 of Python and AWS Lambda"
# https://www.udemy.com/course/aws-automation-with-boto3-of-python-and-lambda-functions/learn/lecture/14614056#overview
# No copyright claimed, no license claimed or granted
#

import boto3
aws_mag_con=boto3.session.Session(profile_name="cfds-dev")
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)


