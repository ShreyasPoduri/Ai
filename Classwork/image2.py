import os
import requests
from PIL import Image
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3"

# Load token from environment (SAFE)
HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise RuntimeError("HF_API_KEY not set")

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json",
}

def generate_image(prompt: str) -> Image.Image:
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))

    raise RuntimeError(
        f"Request failed with status code {response.status_code}: {response.text}"
    )
