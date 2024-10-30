import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SPACE_AND_TIME_API_KEY")


def send_sql(query):
    import requests

    url = "https://proxy.api.spaceandtime.dev/v1/sql"

    headers = {
        "accept": "application/json",
        "apikey": API_KEY,
        "content-type": "application/json"
    }

    data = {
        "sqlText": query,
    }

    response = requests.post(url, headers=headers, json=data)

    return response.text


if __name__ == '__main__':
    print(send_sql("""SELECT * FROM SXT_DAPP_VIEWS.GROWING_ADOPTION
LIMIT 20"""))
