# Create the  table with provisioned capacity
# USAGE:
# python create-table-provisioned TABLE_NAME [RCU WCU default=1]
import boto3
import sys

# Python library (AWS SDK)
# dynamodb = boto3.client('dynamodb')

# Uncomment this line to create table in local
dynamodb = boto3.client("dynamodb", region_name="localhost",
                        endpoint_url="http://localhost:8000")

TABLE_NAME = 'Student'

args = sys.argv[1:]
# TABLE_NAME = args[0]

# Default capacity
RCU = 1
WCU = 1

if len(args) > 2:
    RCU = int(args[1])
    WCU = int(args[2])

# Creates the table
try:
    # Low Level interface for creating a table
    dynamodb.create_table(
        TableName=TABLE_NAME,
        AttributeDefinitions=[
            {"AttributeName": "email", "AttributeType": "S"},
            # {"AttributeName": "name", "AttributeType": "S"},
            # {"AttributeName": "grade", "AttributeType": "N"},
            # {"AttributeName": "course", "AttributeType": "SS"}

        ],
        KeySchema=[
            {"AttributeName": "email", "KeyType": "HASH"},

        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": RCU, "WriteCapacityUnits": WCU}
    )
    print("Table created successfully.")
except Exception as e:
    print("Could not create table. Error:")
    print(e)
