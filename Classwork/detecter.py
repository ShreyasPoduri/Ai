import time, random , requests
from datetime import datetime
from PIL import Image, ImageDraw , ImageFont
import os
from dotenv import load_dotenv
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
if not HF_API_KEY:
    raise RuntimeError("HF_API_KEY not set")


MODEL = "facebook/detr-resnet-50"

API = f"https://router.huggingface.co/models/{MODEL}"

ALLOWED = {".jpg" , ".jpeg" , ".png", ".bmp", ".gif", ".webg", ".tiff"}
MAX_MB = 8

def font(sz = 18):
    for f in ("DejaVuSans.tff", "arial.tff"):
        try:
            return ImageFont.truetype(f,sz)
        except:
            pass

    return ImageFont.load_default()

def ask_image():
    print("\n Pick an image(JPG/PNG/BMP/TIFF ≤ 8) from this folder")
    while True:
        path = input("Image Path: ").strip().strip('"').strip("'")
        if not path or os.path.isfile(path):
            print("file not found")
            continue

        ext = os.path.split(path)[1].lower()
        if ext not  in ALLOWED:
            print("unsupported image type")
            continue                                                                                                   

        if os.path.getsize(path) / (1024 * 1024) > MAX_MB:
            print("File too large!!")
            continue

        try:
            Image.open(path).verify()
        except:
            print("Currupted image.")

        return path
    
def infer(path , image_bytes):
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    
    files = {
        "inputs": (os.path)
    }

    