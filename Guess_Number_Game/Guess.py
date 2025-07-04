import random

def Gues():
    if guess == number:
        print("Congratulations, you guessed it right!")

    elif guess > 100:
        print("Please enter a number between 1 and 100")

    elif guess < 1:
        print("Please enter a number between 1 and 100")

    else:
        print("Sorryyy!!! You lost!")


while True:
    number = random.randint(1, 100)
    guess = int(input("Guess any number between 1 and 100: "))
    Gues()

