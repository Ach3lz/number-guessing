print("Guess the number")
import random 

def guess_the_number():
    number_to_guess = random.randint(1,100)
    attempts = 0 
    max_attempts = 3
    guessed_correct = True

    print("welcome to the Aithusa, guess the number game.")
    print("I have selected a number from 1 to 100. guess the correct number or die")

    while attempts<max_attempts:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess<number_to_guess:
            print("AAh that is too low add more or die")
        elif guess>number_to_guess:
            print("Bend down low")
        else: 
            print("congrats, you wont die after all haha")
            return
       
    print("sorry now you die hahaha")

#start sequence
guess_the_number()