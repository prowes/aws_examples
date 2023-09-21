import boto3
region = 'eu-west-3'
instances = ['i-0a3fd737595a841da']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
