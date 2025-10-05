import re , random
from colorama import Fore , init

init(autoreset=True)

destination = {
    "beaches" : ["Bali" , "Maldives" , "Phuket"],
    "mountains" : ["Swiss Alps" , "Himalayas" , "Rocky mountains"],
    "Cities" : ["Stockholm" , "Paris " , "Tokyo"]
}

jokes = [
    "Why don't programmer like nature? Too many bugs😂" ,
    "Why did the cumputer go to the doctor? Because it had a virus 🤣"
    "What do you call a dinosaur car crash? T-Wreck 😁😹"
]

def normalize_input(text):
    return re.sub(r"\s+" , " " , text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travel Bot: Beaches MOuntains or Cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN + f"How about {suggestion}!")
        print(Fore.CYAN + "Do you like it (yes/no)")
        answer  = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Awsome enjoy {suggestion}")

        elif answer == "no":
            print( Fore.RED + "Travel Bot: Lets try another." )
            recommend()

        else:
            print( Fore.RED + "Travel Bot: I will suggest again." )
            recommend()

    else:
        print(Fore.RED + "Travel Bot: Sorry I don't have that kind of destination ")

    show_help()


def packing_tips():
    print(Fore.CYAN + "Travel Bot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "Travel Bot: How many days?")
    days = input(Fore.YELLOW + "You: ")


    print(Fore.Green + f"Travel Bot: Packing tips for {days} days to {location}:")


