import requests
import config as HF_API_KEY
from colorama import Fore , Style, init

init(autoreset=True)

DEAFAULT_MODEL = "facebook/bart-large-cnn"

def build_api_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"

def query(payload, model_name = DEAFAULT_MODEL):
    
    api_url = build_api_url(model_name)
    headers = {
        "Authorization": f"Bearer{HF_API_KEY}"
    }
    responce = requests.post(api_url , headers=headers , json=payload)
    return responce.json()

def summarized_text(text, min_length ,max_length , model_name = DEAFAULT_MODEL):
    payload = {
        "inputs":text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
        
    }

    print(Fore.BLUE + Style.BRIGHT + f"\n🔍 Performing AI Summarisation using model: {model_name} ")

    result = query(payload , model_name = model_name)

    if isinstance(result, list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error in summarize responce:", result)
        return None
    
if __name__ == "__main__":

    print(Fore.YELLOW + Style.BRIGHT +"👏 Hi there! Whats your name ? ")
    user_name = input("Your name: ").strip() or "User"

    print(Fore.GREEN + f"Welcome, {user_name}! Lets give your text some AI magic!")
    model_choice = 



