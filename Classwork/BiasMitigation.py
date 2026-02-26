from groq import generate_response 

def bias_mitigation_activity():
    print("==== Bias Mitigation Activity ====")
    prompt = input("Enter a prompt to explore bias(Example 'Decribe the ideal doctor)").strip()

    initial_responce = generate_response(prompt, temperature = 0.3, max_tokens=1024)
    print(f"Initial AI responce: {initial_responce}")

   
    if modified_prompt:
        modified_prompt = generate_response(modified_prompt, temperature = 0.3, max_tokens=1024)
        print(f"\Modified AI responce(Neutral): {modified_prompt}")


    else:
        print("No modified prompt entered, skipping this part.")

    
def token_limit_activity():
    print("==== TOKEN LIMIT ACTIVITY ====")
    long_prompt = input("Enter a long prompt(more than 300 word): "
    " can be a story or a decription about something").strip()
    if long_prompt:
     long_responce = generate_response(long_responce, temperature = 0.3, max_tokens=1024)
     preview = (long_responce[:500] + "... ") if len(long_responce) > 500 else long_responce
     print(f"\nModified AI responce(Neutral): {preview}")

    else:   
       print("No pormpt entered skipping long responce!!!")

    short_prompt = input("Now make the prompt more precise: ").strip()
    if short_prompt:
       short_responce = generate_response(short_prompt, temperature = 0.3, max_tokens=1024)
       print(f"\nCondensed prompt: {short_responce}")

    else:   
       print("No prompt entered skipping short responce!!!")

def run_activity():
   print("== AI learning Activity ===")
   print("=== Choose an AI activity ===")
   print("1) Bias mitigation")
   print("2) Token Limits")
   choice = input("> ").strip()

   if choice == 1:
      bias_mitigation_activity()
    
   elif choice==2:
     token_limit_activity()

   else:
      print("Invalid choice please choose opiton 1 or 2")


if __name__ == "__main__":
    run_activity()
    
