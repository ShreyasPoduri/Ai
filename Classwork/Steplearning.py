from groq import generate_response

def run_activity():
    print("ZERO  SHOT, ONE SHOT, FEW-SHOT LEANING ACTIVITY")

    catagory = input("Enter a catagory( eg. animals,/ plant, food, city): ").strip()
    item = input(f"Enter a specific {catagory} to classify: ")

    
    
    zero_shot = f" Is {item} a {catagory} fill in yes or no "
    print("\n  _____________ZERO SHOT LEARNING____________")
    print(f"Responce: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot = f""" Example Catagory:fruit  Item: Apple  Answer: Apple is a fruit.\n 
    Now you try:
    Catagory: {catagory}\n
    Item: {item}\n
    \nAnswer:"""  
    print("\n  _____________ONE SHOT LEARNING____________")
    print(f"Responce: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot =  f""" Example Catagory:fruit  Item: Apple  Answer: Apple is a fruit.\n 
    Now you try:
    Catagory: {catagory}\n
    Item: {item}\n
    \nAnswer:"""  
    print("\n  _____________FEW SHOT LEARNING____________")
    print(f"Responce: {generate_response(few_shot, temperature=0.3, max_tokens=1024)}")

    creative_prompt = f""" Write one sentence story about the given word.\n
    Example 1: Word = moon\n
    Story: THe moon winked att the lovers when they shared thier first kiss.\n

    Word = {item}
    Story = """

    print("\n  _____________CREATIVE FEW SHOT LEARNING____________")
    print(f"Responce: {generate_response(creative_prompt, temperature=0.3, max_tokens=1024)}")

    print("\n ---- Reflection Questions----")
    print("1. How did the responces differ between the different learning activities")
    print("2. Which gave you the moste helpful responce")   
    print("3. How did the example influence the the model's input")

if __name__ == "__main__":
    run_activity()



