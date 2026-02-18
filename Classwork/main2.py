from hf import generate_response
import time

def temperature_prompt_activity():
    print("="* 70)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE + INSTRUCTIONS")
    print("=" * 70)


    print("\n Part 1: TEMPERATURE EXPLORATION")

    base = input("Enter a creative prompt").strip()

    for t , label in [(0.1, "LOW (0.1) - Deraminitistic" )
                      (0.1, "MEDIUM (0.1) - Balanced" )
                      (0.1, "High (0.9) - Creative" )]:
        print(f"\n --- {label} ---")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)


    print("\n PART 2: INSTRUCTION BASED PROMPTS")
    topic = input("choose a topic (ex. climate change, space exploration etc )").strip()
    
    prompts = [f" summarize key facts about {topic} in 3 or 4 sentences. " ,
                 f"Explain {topic} as if I am a 10 year old!", 
                 f" Write pros/cons about {topic}"
                 f"Create  a fictional newsheadline from about 2050!! "]
    
    for i, p in enumerate(prompts, 1):
        print(f"\n---{"instructions"}---\n{p}")
        print(generate_response(base, temperature=t, max_tokens=512))
        time.sleep(1)

   
    print("\n   YOUR OWN INSTRUCTION BASED PROMPT! ")
    custom = input("Enter your inctructuin based prompt!")
  
    try:
        temp = float(input("Set temperature(0.1 to 1.0): ").strip())

        if not (0.1 <= temp <= 1.0):ValueError

    except ValueError: 
        print("invalid temperature. Using 0.7")