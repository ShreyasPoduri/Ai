print("Hello I am an AI chatbot , nice to meet you.")
name = input("What's your name ?")

print(f"Nice to meet you {name}")

mood = input("How as your day(Good / Bad)").lower()

if mood == "good":
    print("Thats nice , have a good day.")

elif mood == "bad":
    print("It's ok , Will be sorted out in some time")

else:
    print("Sometimes your feeling can me too difficult to express. It's ok")


need = input("Anything else you want me to do")

if need == "no":
    print("Ok then ,Bye")

elif need == "Yes":
    print("Cant help right now sry :(")

else:
    print("")


print(f"NIce to meet you {name} , Bye Bye")