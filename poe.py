from dotenv import load_dotenv
import os
from poe_api_wrapper import AsyncPoeApi
import asyncio

load_dotenv()


tokens = {
    'p-b': os.getenv("POE_P_B"),
    'p-lat': os.getenv("POE_P_LAT"),
}


async def main(message="Explain quantum computing in simple terms"):
    client = await AsyncPoeApi(tokens=tokens).create()
    async for chunk in client.send_message(bot="gpt4_o", message=message):
        print(chunk["response"], end='', flush=True)


if __name__ == '__main__':
    asyncio.run(main())