import sys
import langchain
import json
import logging

def handler(event, context):

    event_as_string = json.dumps(event)
    data = json.loads(event_as_string)

    print(f"Event looks like: {data}")

    message = {
    'message': 'Flash agent at your service!'
    }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }