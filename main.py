import random



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices
game_images = [rock, paper, scissors]

# User input
chosen_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Validate input
if chosen_number not in [0, 1, 2]:
    print("Invalid input! Please choose 0, 1, or 2.")
else:
    # Display user's choice
    print("You chose:")
    print(game_images[chosen_number])

    # Computer's choice
    computer_number = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_number])

    # Determine the winner
    if chosen_number == computer_number:
        print("It's a draw!")
    elif (chosen_number == 0 and computer_number == 2) or \
         (chosen_number == 1 and computer_number == 0) or \
         (chosen_number == 2 and computer_number == 1):
        print("You win!")
    else:
        print("You lose!")