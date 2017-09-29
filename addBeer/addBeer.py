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
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        },
    }

def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    print(event)
    bodyJson=json.loads(event['body'])

    response = client.scan(
        TableName='DavisBarApp'
    )
    print("test")
    print(response)
    processUpdate = False
    for row in response['Items']:
        print(row['Name']['S'])
        if row['Name']['S'] == bodyJson['Name']:
            print(row['PIN']['N'])
            if row['PIN']['N'] == bodyJson['PIN']:
                beerCount = int(row['BeerCount']['N'])
                print(beerCount)
                processUpdate = True

    beerCount = beerCount + 1

    response = client.update_item(
        ExpressionAttributeNames={
            '#B': 'BeerCount',
        },
        ExpressionAttributeValues={
            ':b': {
                'N': str(beerCount)
            },
        },
        Key={
            'Name': {
                'S': bodyJson['Name'],
            }
        },
        ReturnValues='ALL_NEW',
        TableName='DavisBarApp',
        UpdateExpression='SET #B = :b'
    )

    return respond(None, response)
