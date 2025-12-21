import requests

API_KEY = "YOUR_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "inputs": "Hello world, please summarize this."
}

r = requests.post(
    "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
    headers=headers,
    json=payload
)

print(r.status_code)
print(r.json())
