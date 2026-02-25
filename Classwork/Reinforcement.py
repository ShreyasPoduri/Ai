from groq import generate_response

def reinforcement_learning_activity():
    print("\n=== Reinforcement Learning Activity ===\n")
    prompt = input("Enter a prompt for the ai model(e.g  , 'Decribe a lion')").strip()


    
    initial_responce = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\n Initial responce: {initial_responce}")


    try:
        rating = int(input("Rate the responce from 1(bad) to 5(good): ").strip())

        if rating < 1 or rating > 5:
            print("Invalid responce. Using 3 (neutral)")
            rating = 3

    except ValueError:
        print("Invalid responce. Using 3 (neutral)")
        rating = 3

        feedback = input("Provide feedback for improvment: ").strip()
        improved_responce = f"{initial_responce} improved with your feedbacck: {feedback}"
        print(f"Imporved AI responce: {improved_responce}")

        print("\n Refection")
        print("1. How did the models responce improve feedback ")
        print("2. How does reinforcement learning hel ai improve its performance over time")


def role_based_activity():
    print("\n=== Role Based Activity ===\n")
