import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client('lambda')

list_response = client.list_functions()

for function in list_response['Functions']:
    try:
        policy_response = client.get_policy(
            FunctionName=function['FunctionName']
        )
        policy = json.loads(policy_response['Policy'])
        print(function['FunctionName'] + ":")
        for statement in policy['Statement']:
            print("\t" + statement['Principal']['Service'])
    except ClientError:
        # do nothing it means there is no policy
        print(function['FunctionName'] + ": \r\n\tNo policies for this function")
