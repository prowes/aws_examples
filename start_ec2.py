import boto3
region = 'eu-west-3'
instances = ['i-0a3fd737595a841da']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
