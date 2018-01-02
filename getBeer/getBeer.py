import boto3
import json
import os
import re
import time
import ast
from botocore.client import Config
from botocore.exceptions import ClientError

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err['message'] if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
        },
    }

def lambda_handler(event, context):
    client = boto3.client('dynamodb')

    response = client.scan(
        TableName='DavisBarApp-BeersOnTap'
    )

    return respond(None, response)
