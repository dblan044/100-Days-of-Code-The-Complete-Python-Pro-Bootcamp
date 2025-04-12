import random, art

def random_int():
    return random.randint(1, 100)

def easy_or_hard_mode(turns, num):
    """Function to provide turns based on difficulty and comparison between user guess and correct int"""

    #count down from the number of turns by 1 until 0
    for attempts in range(turns, 0, -1):
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess == num:
            print(f"You got it! The answer was {num}")
            return
        elif user_guess > num:
            print("Too high!")
        else:
            print("Too low!")

        if attempts > 1:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose!.")
            return

def guess_number():
    """Function to play the guess the number game"""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        easy_or_hard_mode(10, random_int())

    if difficulty == "hard":
        easy_or_hard_mode(5, random_int())

guess_number()