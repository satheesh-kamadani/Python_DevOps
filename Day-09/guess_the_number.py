# Guess the number between 1 to 100
import random

number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess the number between 1 to 100: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high")
    else:
        print("Congratulation you guessed it")

    