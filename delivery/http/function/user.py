import json

def list(event, context):
    body = { "message": "this is users list" }
    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
