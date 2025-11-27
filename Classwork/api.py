import requests

def random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
     
    if response.status_code ==200:
        print(f"Full JSON Responce: {response.json()}")

        joke_data = response.json()
        return f"{joke_data['setup']}-{joke_data['punchline']} "
    else:
        return "Failed to retreive joke"
    
def main():
    print("Welcome to joke generator")

    while True:
        user_input = input("Press Enter to get a joke and type 'q'/exit to quit ").strip().lower

        if user_input in ("q",'exit'):
            print("Goodbye")
            break

        joke  = random_joke()
        print(joke)

if __name__ == "__main__":
 main()
