import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to sentiment spy! :) {Style.RESET_ALL}")

username = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not username:
    username = "Mystery User"

conversation_history = []

print(f"\n{Fore.CYAN}Hello Agent {username}!")
print("Type a sentence and I will tell you the sentiment !!! ☆*: .｡. o(≧▽≦)o .｡.:*☆")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}->> {Style.RESET_ALL} ").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter text or any valid command.{Style.RESET_ALL}")
        continue

    # ---- Exit ----
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}Exiting Sentiment Spy. Farewell Agent {username}!{Style.RESET_ALL}")
        break

    # ---- Reset ----
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.BLUE}All conversation history cleared! 😊{Style.RESET_ALL}")
        continue

    # ---- History ----
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet. 😐{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}🗺️ Conversation history:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😢"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}-{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # ---- Sentiment Analysis ----
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}-{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
