import random as rd

def check(comp, user):
    if(comp ==  user):
        print("Its a DRAW!")
    elif(comp == "Snake" and user == "Water"):
        print("You LOSE!")
    elif(comp == "Gun" and user == "Snake"):
        print("You LOSE!")
    elif(comp == "Water" and user == "Gun"):
        print("You LOSE!")
    else:
        print("You WON!")

def exit_game():
    print("👋 Thanks for playing! Goodbye.")
    exit()


while True:
    options = ["Snake", "water","Gun"]
    user = input("Enetr Snake, Water or Gun \n Your choice:")
    comp = rd.choice(options)
    check(comp, user)
    print("Your choice:", user)
    print("Computer's choice:", comp)
    print("Enter \"quit\" or \" exit \" to exit the game")
    if user.lower() in ["exit", "quit"]:
         exit_game()
