import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLTable')

def lambda_handler(event, context):
    code = event.get("rawPath", "/").lstrip("/")

    response = table.get_item(Key={"shortCode": code})

    if "Item" not in response:
        return {"statusCode": 404, "body": "URL not found"}

    return {
        "statusCode": 301,
        "headers": {
            "Location": response["Item"]["originalUrl"]
        }
    }
