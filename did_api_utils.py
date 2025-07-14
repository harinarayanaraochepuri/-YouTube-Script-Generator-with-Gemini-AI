import requests
import os
from dotenv import load_dotenv

load_dotenv()

def create_did_video(text_script):
    url = "https://api.d-id.com/talks"
    headers = {
        "Authorization": f"Bearer {os.getenv('DID_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "script": {
            "type": "text",
            "input": text_script
        },
        "source_url": "https://models.d-id.com/amy"  # Change avatar
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()
