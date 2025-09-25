import colorama

from colorama import Fore , Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to centiment spy! :) {Style.RESET_ALL}")

username = input(f"{Fore.MAGENTA} PLease enter your name:  {Style.RESET_ALL}").strip()

if not username:
    username = "Mystery User"

conversation_history = []

print(f"\n {Fore.CYAN} Hello Agent {username}!")
print("Type a sentece and I will tell you the sentiment !!! ☆*: .｡. o(≧▽≦)o .｡.:*☆")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN} , {Fore.YELLOW}'History' {Fore.CYAN}" 
      f"or {Fore.YELLOW}'Exit'{Fore.CYAN} , to quit {Style.RESET_ALL}\n"  )

while True:
    user_input = input(f"{Fore.GREEN}->> {Style.RESET_ALL} ").strip()

    if not user_input:
        print(f"{Fore.RED} Please enter text or any valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower == "exit":
        print(f"{Fore.BLUE}Exiting sentiment Spy. Farwell Agent {username}!{Style.RESET_ALL}")

    if user_input.lower == "reset":
        conversation_history.clear()
        print(f"{Fore.BLUE}Exiting sentiment Spy. Farwell Agent {username}!{Style.RESET_ALL}")

