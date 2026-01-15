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
    
    caption = result[0].get("generated text", "No caption generated.")
    return caption


def generate_text(prompt, model = "gpt2", max_new_token = 60):
    print(f"{Fore.CYAN}??????? Generate text with prompt{prompt} ")
    api_url = f"https://api-inference.huggingface.co/models/{model}"
    payload = {"inputs":prompt,"parameters":{"max_new_tokens": max_new_token}} 
    text_bytes = query_hf_api(api_url, payload=payload)
    try:
        result = json.loads(text_bytes.decode("utf-8"))

    except Exception as e:
        raise Exception("Failed to decode text generation responce.")
    if isinstance(result, dict) and "error" in result:
        raise Exception(result["error"])
    
    generated = result[0].get("generate_text","")
    return generated

def truncate_text(text, word_limit):
    print(f""" {Style.BRIGHT}
          {Fore.GREEN}====================== Image-to-Text Conversation==============================
          Select output type:
          1. Caption(5 words)
          2. Description(30 words)
          3.Summary(50 words)
          4.Exit
          ============================================================================================
          """)

def main():a
    image_path = input(f"{Fore.BLUE}Enter a pth of the image fro text generation(eg., test.jpg):{Style.RESET_ALL}")
    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ The file '{image_path} does not exist")
        return
    try: 
        image = Image.open(image_path)

    except Exception as e : 
        print(F"{Fore.RED}❌ Failed to open image:{e}")
        return
    
    basic_caption = get_basic_caption(image)
    print(F"{Fore.YELLOW}???")

            








