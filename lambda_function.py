import sys

from flask import Request
import langchain
import json
import logging
import asyncio

from flash_agent.agent.async_agent import AsyncAgent

async def async_handler(event, context):

    # event_as_string = json.dumps(event)
    data = json.loads(event)
    

    print(f"Event looks like: {data}")

    # Need to parse `body` when it's an API request, but this lambda
    #   is currently being invoked from the lambda client directly on `boto3`.
    # body = json.loads(data['body'])
    # print(f"Body looks like: {body}")

    """
    There are two types of `request`s, `validate` and `generate`. 
    They are passed in the "request_type" variable.
    """

    request_type = data["request_type"]
    technology = data["technology"]

    if request_type == Request.GENERATE.value:
        print("Recieved a GENERATE lambda call, ")
    
        model = data["model"]

        print(f"Technology we are generating for is {technology}, using model {model}.")

        agent = AsyncAgent(technology)

        result = await agent.generate_full_async()

        message = {
        'message': f'Flash agent which knows about {technology} is at your service!',
        'learning_material': result
        }

        return result, message

    elif request_type == Request.VALIDATE.value:
        print(f"Recieved a VALIDATE lambda call, for technology {technology}")

    else:
        print(f"ERROR: Recieved a non-defined request type: {request_type}")
        message = {
            'message': f'Your request of type {request_type} was not defined. Please try again with either "generate" or "validate".'
        }
        return "", message



def handler(event, context):

    result, message = asyncio.run(async_handler(event, context))

    print(f"Agent has finished running.")
    # print(result)

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }