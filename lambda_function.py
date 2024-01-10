import sys
import langchain
import json
import logging

def handler(event, context):

    event_as_string = json.dumps(event)
    data = json.loads(event_as_string)

    logging.info(f"Event looks like: {data}")

    message = {
    'message': 'Execution started successfully!'
    }
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }


    return 'Hello from AWS Lambda using Python' + sys.version + '!'


# 799492718470.dkr.ecr.us-west-2.amazonaws.com/flash-agent