import requests
import time
from config import HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)

f= Fore
s = Style

default_model = "facebook/bart-large-cnn"

def build_api_url(model_name):
    return f"https://router.huggingface.co/hf-inference/models/%7Bmodel_name%7D"

def query(payload, model_name):
    url = build_api_url(model_name)

    headers = {
        "Authorization" : f"Bearer" {HF_API_KEY},
        "Content-Type"  : "application/json"

    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
    except requests.exceptions.RequestException as e:
            
            print(f.RED + "Network error: " e)
            return None
    if response.status_code == 200:

            print(f.RED + f"HTTP {response.status_code}")
            print(f.RED + response.text)
            return None
    

    try:
          data = response.json()
    except ValueError:
           print(f.RED + "Responce was not JSON:")
           print(f.RED + response.text)
           return None
    
    return data


def summarize(text, min_len, max_len, model ):
    payload = {
          "inputs" : text,
          "parameters" : {
                "min_length": min_len,
                "max_length" : max_len
          }
    }
    