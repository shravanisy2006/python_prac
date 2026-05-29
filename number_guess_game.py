#Type 1

import random
print("Welcome to the number guessing game: ")
print("Note that you only have 5 choices: ")
num=random.randint(1,10)
choice = 5

while choice !=0:
    guess=int(input("Please enter your guess: "))
    if (guess == num):
        choice-=1
        print("You guess it right!")
        choice=0
    else:
        choice-=1
        print("You are wrong.")

        if (choice == 0):
            print("Oh! you are out of guesses..")


#Type 2

import random
print("Welcome to the number guessing game: ")
print("Note that you only have 5 choices: ")
num=random.randint(1,10)
choice = 5

while choice !=0:
    guess=int(input("Please enter your guess: "))
    if (guess == num):
        choice-=1
        print("You guess it right!")
        choice=0
    else:
        choice-=1
        print(f"You are wrong.you have {choice} left.")
        
        if (choice == 0):
            print("Oh! you are out of guesses..")
        else:
            if (guess < num):
                print("Guess higher number.")
            else:
                print("Guess lower number.")
