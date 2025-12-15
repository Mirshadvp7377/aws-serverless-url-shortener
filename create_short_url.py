import json
import random
import string
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLTable')

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    original_url = body.get("url")

    if not original_url:
        return {"statusCode": 400, "body": "URL is required"}

    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    table.put_item(Item={
        "shortCode": short_code,
        "originalUrl": original_url
    })

    return {
        "statusCode": 200,
        "body": json.dumps({
            "shortCode": short_code,
            "shortUrl": f"https://<REDIRECT_FUNCTION_URL>/{short_code}"
        })
    }
