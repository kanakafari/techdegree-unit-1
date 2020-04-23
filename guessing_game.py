"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

high_score = [10]

def start_game():
    header = "-" * 36
    print(header, "\nWelcome to the number guessing game!")
    print(header)
    win_number = random.randint(1,10)
    num_range = [1,2,3,4,5,6,7,8,9,10]
    guess = 0
    guess_counter = 0
    while win_number != guess:
        try:
            guess = int(input("Please guess a number between 1-10: "))
            if guess not in num_range:
                raise ValueError
        except ValueError:
            print("Oh no! Please select a valid number.")
            continue
        if guess > win_number:
            print("It's lower")
        elif guess < win_number:
            print("It's higher")
        guess_counter += 1
    if guess_counter < high_score[-1]:
        high_score.append(guess_counter)
    print("Got it! It took you {} attempts.".format(guess_counter))
    print("The High Score is {} attempts!".format(high_score[-1]))
    play_again = input("Would you like to play again? [y]es/[n]o: ")
    if play_again.lower() == "y":
        start_game()
    else:
        print("Game Over. Thanks for playing!")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
