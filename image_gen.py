import base64
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
def image_generator(prompt):
    load_dotenv()

    engine_id = os.getenv("STABLE_DIFFUSION_ENGINE_ID")
    api_host = os.getenv("STABLE_DIFFUSION_API_HOST")
    api_key = os.getenv("STABLE_DIFFUSION_API_KEY")

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": f"A person wearing : {prompt}"
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    for i, image in enumerate(data["artifacts"]):
        return base64.b64decode(image["base64"])
