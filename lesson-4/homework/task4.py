import random

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the number guessing game!")
    print("I have selected a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    while attempts<max_attempts:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts}. Enter your guess: "))

        if guess<number_to_guess:
            print("Too low")
        elif guess>number_to_guess:
            print("Too high!")
        else:
            print("You guessed it right!")
            break
        attempts+=1

    if attempts==max_attempts:
        print(f"You lost! The correct number was {number_to_guess}.")
        play_again()

def play_again():
    response = input("Want to play again? (Y/YES, y, yes, ok): ").lower()

    if response in ['y', 'yes', 'ok']:
        start_game()
    else:
        print("Thanks for playing! Goodbye.")

start_game()
