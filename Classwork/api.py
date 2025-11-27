import requests

def random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
     
    if response.status_code ==200:
        print(f"Full JSON Responce: {response.json()}")

        joke_data = response.json
        return f"{joke_data['setup'] - {joke_data['punchline']}} "
    else:
        return "Failed to retreive joke"