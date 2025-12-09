import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_fact(category):
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json()
        
        print(f"\n{category.capitalize()} fact: {fact['text']}\n")
    else:
       
        print("Failed to fetch fact")

def menu():
    print("Choose a category:")
    print("1. Technology")
    print("2. History")
    print("3. Science")
    print("4. Space")

    choice = input("Enter 1, 2, 3 or 4: ")
    if choice == "1":
        return "technology"
    
    elif choice == "2":
        return "history"
    elif choice == "3":
        return "science"
    elif choice == "4":
     
        return "space"
    else:
        return "technology"

category = menu()
while True:
    userInput = input("Press ENTER to get a fact or type 'q' to quit: ")
    if userInput.lower() == "q":
        break
    get_fact(category)
