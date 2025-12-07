import requests
from config import HF_API_KEY   
from colorama import Fore, Style, init

init(autoreset=True)

DEFAULT_MODEL = "facebook/bart-large-cnn"   

def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name=DEFAULT_MODEL):
    api_url = build_api_url(model_name)
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"   
    }
    response = requests.post(api_url, headers=headers, json=payload)  
    return response.json()

def summarize_text(text, min_length, max_length, model_name=DEFAULT_MODEL):  
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }

    print(Fore.BLUE + Style.BRIGHT + f"\n🔍 Performing AI Summarisation using model: {model_name} ")

    result = query(payload, model_name=model_name)

    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error in summarize response:", result)  
        return None

if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "👏 Hi there! What's your name?")
    user_name = input("Your name: ").strip() or "User"

    print(Fore.GREEN + f"Welcome, {user_name}! Let's give your text some AI magic!")
    model_choice = input("Model name (leave blank for default): ").strip() or DEFAULT_MODEL

    print(Fore.YELLOW + "\nPaste the text you want to summarize:")
    text_to_summarize = input("\nYour text:\n")

    print(Fore.YELLOW + "\nEnter minimum summary length:")
    min_len = int(input("Min length: "))

    print(Fore.YELLOW + "Enter maximum summary length:")
    max_len = int(input("Max length: "))

    # Perform summarization
    summary = summarize_text(text_to_summarize, min_len, max_len, model_choice)

    if summary:
        print(Fore.GREEN + "\n✨ Summary:")
        print(Fore.CYAN + summary)
