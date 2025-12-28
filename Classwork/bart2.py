
import requests
import time
from config import HF_API_KEY
from colorama import Fore, Style, init

init(autoreset=True)


F = Fore
S = Style

DEFAULT_MODEL = "facebook/bart-large-cnn"


def build_api_url(model_name: str) -> str:
    return f"https://router.huggingface.co/hf-inference/models/{model_name}"


def query(payload: dict, model_name: str):
    url = build_api_url(model_name)

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
    except requests.exceptions.RequestException as e:
        print(F.RED + "Network error: " + str(e))
        return None

    if response.status_code != 200:
        print(F.RED + f"HTTP {response.status_code}")
        print(F.RED + response.text)
        return None

    try:
        data = response.json()
    except ValueError:
        print(F.RED + "Response was not JSON:")
        print(F.RED + response.text)
        return None

    return data


def summarize(text: str, min_len: int, max_len: int, model: str = DEFAULT_MODEL):
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_len,
            "max_length": max_len,
        },
    }

    print(F.BLUE + S.BRIGHT + f"\nUsing model: {model}")
    result = query(payload, model)

    if result is None:
        return None

    if isinstance(result, dict) and "error" in result:
        err = result["error"]
        if isinstance(err, str) and "loading" in err.lower():
            print(F.YELLOW + "Model loading... waiting 10 seconds")
            time.sleep(10)
            return summarize(text, min_len, max_len, model)
        else:
            print(F.RED + "API Error: " + str(err))
            return None

    if isinstance(result, list) and result:
        first = result[0]
        if isinstance(first, dict) and "summary_text" in first:
            return first["summary_text"]

    print(F.RED + "Unexpected response: " + str(result))
    return None


if __name__ == "__main__":
    print(F.YELLOW + S.BRIGHT + "Enter text to summarize:")
    try:
        text = input("> ").strip()
    except EOFError:
        text = ""

    if not text:
        print(F.RED + "No text entered.")
        exit(1)

    summary = summarize(text, 40, 100, DEFAULT_MODEL)

    if summary:
        print(F.GREEN + S.BRIGHT + "\nSummary:\n")
        print(F.CYAN + summary)
    else:
        print(F.RED + "\nSummarization failed.")
from colorama import Fore, Style, init
