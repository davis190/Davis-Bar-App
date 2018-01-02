# Bar App (Lambda + Api Gateway + DynamoDB + Cloudformation)

This is a base tracking application. It is used for a bar app to track amount of beer consumed. It uses Lambda APIs to pull data from dynamo. The HTML web page interacts with it though a set of API Gateway APIs.

## File explaination
- cf.template.yml - This file is a CloudFormation template that creates lambda functions from the pythong files in the folders.
- addBeer, getPeople and getBeer - Python functions for lambda that will act as the API and interaction with the Dynamo tables
- html - The folder of HTML files. Could be a single page app but split out some config variables to not check them into GitHub.

## DynamoDB Table(s)
DavisBarApp
- Name - primary key
- BeerCount
- PIN

DavisBarApp-BeersOnTap
- TapPosition - primary key
- Beer

DavisBarApp-BeersDrank
- Timestamp - primary key
- Beer
- Person

## Setup and maintain the stack

### Prep Steps
1. https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/
2. Create bucket in the account & Set up usage plan / API key

### Deploy initial app
1. aws cloudformation package --s3-bucket $s3BucketName --template-file cf.template.yml --output-template-file cf.yml --profile $localCredentialsProfile
2. aws cloudformation deploy --template-file cf.yml --stack-name $nameOfStack --capabilities CAPABILITY_IAM --profile $localCredentialsProfile

### Delete stack
1. aws cloudformation delete-stack --stack-name $nameOfStack  --profile $localCredentialsProfile


## Current Manual steps
- Associating API key/usage plan with API
- Creating and populating DynamoDB tables



