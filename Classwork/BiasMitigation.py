from groq import generate_response


def bias_mitigation_activity():
    print("==== Bias Mitigation Activity ====")
    prompt = input("Enter a prompt to explore bias (Example 'Describe the ideal doctor'): ").strip()

    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"Initial AI response: {initial_response}")

    modified_prompt = input("Enter a modified/neutral prompt (or leave blank to skip): ").strip()
    if modified_prompt:
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"Modified AI response (Neutral): {modified_response}")
    else:
        print("No modified prompt entered, skipping this part.")

    
def token_limit_activity():
    print("==== TOKEN LIMIT ACTIVITY ====")
    long_prompt = input("Enter a long prompt (more than 300 words): "
                        "can be a story or a description about something").strip()
    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500] + "... ") if len(long_response) > 500 else long_response
        print(f"\nModified AI response (Neutral): {preview}")
    else:
        print("No prompt entered skipping long response!!!")

    short_prompt = input("Now make the prompt more precise: ").strip()
    if short_prompt:
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nCondensed prompt: {short_response}")
    else:
        print("No prompt entered skipping short response!!!")

def run_activity():
    print("== AI learning Activity ===")
    print("=== Choose an AI activity ===")
    print("1) Bias mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice please choose option 1 or 2")


if __name__ == "__main__":
    run_activity()
    
