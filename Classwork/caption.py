import requests
import os
from dotenv import load_dotenv
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise RuntimeError("HF_API_KEY not set")


MODEL = "Salesforce/blip-image-captioning-base"
API = f"https://router.huggingface.co/models/{MODEL}"

header = {
    "Authorization" : f"Bearer {HF_API_KEY}"
}

def caption_single_image():
    image_source = "image.png"

    try:
        with open(image_source,  "rb") as f:
            files = {"file" : f}
            responce = requests.post(API, headers=header, files= files)

    except Exception as e:
        print(f"Cou1dn't load image from {image_source}\nError: {e}")
        return  
    

    if responce.status_code != 200:
        print(f"HTTP {responce.status_code}")
        print(responce.text)
        return None
    
    try:
        result = responce.json()
    except Exception as e:
        print("JSON parsing failed")
        print("Raw responce:", responce.text)
        return
    
    caption = result[0].get("generated_text", "No caption found")

    print("Image:", image_source) 
    print("Caption:", caption)

def main():
    caption_single_image

if __name__ == "__main__":
    main()