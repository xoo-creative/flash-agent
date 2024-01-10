import sys
import langchain
import json
import logging
import asyncio

from flash_agent.agent.async_agent import AsyncAgent

async def async_handler(event, context):

    event_as_string = json.dumps(event)
    data = json.loads(event_as_string)

    print(f"Event looks like: {data}")
    body = json.loads(data['body'])
    print(f"Body looks like: {body}")

    technology = body["technology"]

    print(f"Technology we are generating for is {technology}.")

    agent = AsyncAgent(technology)

    result = await agent.generate_full_async()

    message = {
    'message': f'Flash agent which knows about {technology} is at your service!',
    'learning_material': result
    }

    return result, message


def handler(event, context):

    result, message = asyncio.run(async_handler(event, context))

    print(f"Agent has finished running.")
    # print(result)

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }