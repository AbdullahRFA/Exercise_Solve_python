# snake, water and gun is a variations of children's game "Rock-paper-scissors" where players use hand gestures to
# represent a snake, water and gun. The gun beats the snake, the water beats the gun, and the snake beats the water

# write a python program to create a snake water Gun game in python using if-else statements. Do not create any fancy GUI.
# USE PROPER functions to check for win.

import random

# Define the choices for the game
game = ["snake", "water", "gun"]


def play_game(reply):
    """
    Function to play the Snake, Water, Gun game.
    It compares the player's choice with the computer's choice and declares the result.
    """
    # Randomly select the computer's choice
    computer_choice = random.choice(game)

    # Check for a draw
    if reply == computer_choice:
        print(f"\nGame Draw! You both chose {reply}.")
    # Check for win or lose conditions
    elif (reply == 'gun' and computer_choice == 'snake') or \
            (reply == 'snake' and computer_choice == 'water') or \
            (reply == 'water' and computer_choice == 'gun'):
        print(f"\nComputer chose {computer_choice}, so you win!")
    else:
        print(f"\nComputer chose {computer_choice}, so you lose!")


# Main game loop
while True:
    # Prompt the user for their choice
    reply = input("\nEnter your choice (snake, water, gun) or press 'q' to quit: ").strip().lower()

    # Exit the game if the user types 'q'
    if reply == 'q':
        print("\nThank you for playing! Goodbye!")
        break

    # Validate the input
    if reply not in game:
        print("\nInvalid choice! Please enter 'snake', 'water', or 'gun'.")
        continue  # Restart the loop if input is invalid

    # Call the play_game function with the user's choice
    play_game(reply)