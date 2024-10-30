import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("SPACE_AND_TIME_ACCESS_TOKEN")


def send_sql(query):
    url = "https://api.spaceandtime.dev/v1/sql"

    payload = {
        "sqlText": query
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


if __name__ == '__main__':
    send_sql("""SELECT * FROM SXT_DAPP_VIEWS.GROWING_ADOPTION
LIMIT 20""")
