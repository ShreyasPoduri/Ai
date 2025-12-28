import os
import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable not set")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

text = "I love this movie! It was fantastic!!"

response = requests.post(API_URL, headers=headers, json={"inputs": text})

if response.status_code == 200:
    result = response.json()
    label = result[0][0]["label"]
    score = result[0][0]["score"]

    print("Sentiment:", label)
    print("Score:", score)
else:
    print("Error:", response.status_code, response.text)
