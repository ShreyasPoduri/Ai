import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def random_tech_fact():
    responce = requests.get(url)

    if responce.status_code == 200:
        fact_data = responce.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print("Failed to fetch fact")

while True:
    userInput = input("Press ENTER to get a random tech fact and press 'q' to quit")
    if userInput.lower == 'q':
        break

    random_tech_fact()

