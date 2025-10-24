import random

def rolldice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

    print(f"({dice_1}/{dice_2})")

while True:
    user = input("do you wanna roll dice (y/n): ").lower()

    if user == "y":
        rolldice()
    else:
        print("thanks for your answer")
        break


    
    
