import boto3

aws_mag_con=boto3.session.Session(profile_name="developer")

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