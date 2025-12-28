import requests 
from PIL import Image
from io import BytesIO
from config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def generate_image_from_text(promt:str)-> Image.Image:
    headers = {"Autorization" : f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs" : promt
    }

    try:

        responce = requests.post(API_URL, headers=headers, json = payload, timeout= 30)
        responce.raise_for_status()

        if 'image' in responce.headers.get('Content - Type',''):
            image = Image.open(BytesIO(responce.content))
            return image
        else:
            raise Exception('The responce is not an image, It might me an error message.')
    except :
        print("hu")