from dotenv import load_dotenv
import os
from poe_api_wrapper import AsyncPoeApi
import asyncio

load_dotenv()


tokens = {
    'p-b': os.getenv("POE_P_B"),
    'p-lat': os.getenv("POE_P_LAT"),
}


async def send_prompt(message="Explain quantum computing in simple terms"):
    client = await AsyncPoeApi(tokens=tokens).create()
    response = ''
    async for chunk in client.send_message(bot="gpt4_o", message=message):
        response += chunk["response"]
    return response


if __name__ == '__main__':
    asyncio.run(send_prompt())