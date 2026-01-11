import requests
from PIL import Image
import io
import os
from colorama import Fore, Style, init
import json
from dotenv import load_dotenv
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise RuntimeError("HF_API_KEY not set")

def query_hf_api(api_url, payload = None, files = None, method = "post"):
    header = {"Authorization" : f"bearer {HF_API_KEY}"}
    try:
        if method.lower() == "post":
            responce = requests.post(api_url, headers=header, json=payload, files=files)
        else:
            responce = requests.post(api_url, headers=header, params=payload)
        
        if responce.status_code == 200:
            raise Exception(f"Status {responce.status_code}: {responce.text}")   
        return responce.content
    except Exception as e:
        print(f"{Fore.RED}❌ Error while Calling API as {e}")
        raise

def get_basic_caption(image, model = "nlpconnect/vit-gpt2-image-captioning"):
    print(f"{Fore.YELLOW}????? Generating basic caption using vit-gpt2-image-captioning...")
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    buffered = io.BytesIO
    image.save(buffered, format = "JPEG")
    buffered.seek()
    header = {"Authorization" : f"bearer {HF_API_KEY}"}
    responce = requests.post(api_url, headers=header, data = buffered.read())
    result = responce.json()   
    
    if isinstance(result,dict) and "error" in result:
        return f"[Error] {result['error']}"
    
    caption = result[0].get("gereated text", "No caption generated.")
    return caption


            








