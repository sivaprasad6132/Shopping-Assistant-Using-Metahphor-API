import requests
import os
from dotenv import load_dotenv
import json

def shop_link_metaphor_api(query,domains):
    api_key = os.getenv("METAPHOR_API_KEY")
    url = "https://api.metaphor.systems/search"

    payload = {
        "query": str(query),
        "includeDomains": domains,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": "f6ec1167-8554-44b0-84c1-8f6a08c1cbcf",
    }

    response = requests.post(url, json=payload, headers=headers)

    shop_data = []
    response_data = json.loads(response.text)
    for item in response_data["results"]:
        shop_data.append([item["title"],item["url"]])
    return shop_data