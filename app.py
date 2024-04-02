# build a rock, paper, or scissors game between one user and the computer

import random

def rock_paper_scissors(player_score):
    valid_choices = False
    while valid_choices == False:
        # get the user's choice
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        # check if the user's choice is valid
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
        else:
            valid_choices = True
    # get the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # print the computer's choice
    print(f"Computer chose: {computer_choice}")
    # determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        rock_paper_scissors(player_score)
    else:
        print(f"Your score is: {player_score}")

rock_paper_scissors(0)

