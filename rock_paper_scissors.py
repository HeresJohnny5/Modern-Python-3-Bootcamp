from random import randint

print("...rock...\n...paper...\n...scissors...")
print("Enter 1: One Player")
print("Enter 2: Two Players")

players = input()

def game_logic():
  player_2 = None

  if players == "1":
    player_2 = "CPU"
  else:
    player_2 = "Player 2"

  if player_2 == "CPU":
    player_1_input = input("Player 1: Enter choice\n").lower()

    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = computer_choices[randint(0, 2)]

    print(f"CPU Chooses {computer_choice}")

    if player_1_input == computer_choice:
      print("The game is a time.")
    elif player_1_input == "rock" and computer_choice == "scissors":
      print("Player 1 wins")
    elif player_1_input == "paper" and computer_choice == "rock":
      print("Player 1 wins")
    elif player_1_input == "scissors" and computer_choice == "paper":
      print("Player 1 wins")
    else:
      print("CPU Wins")
  elif player_2 == "Player 2":
    player_1_input = input("Player 1: Enter choice\n").lower()

    player_2_input = input("Player 2: Enter choice\n").lower()

    if player_1_input == player_2_input:
      print("The game is a time.")
    elif player_1_input == "rock" and player_2_input == "scissors":
      print("Player 1 wins")
    elif player_1_input == "paper" and player_2_input == "rock":
      print("Player 1 wins")
    elif player_1_input == "scissors" and player_2_input == "paper":
      print("Player 1 wins")
    else:
      print("Player 2 wins")

game_logic()

# if players == "1":
#   player_1_input = input("Player 1: Enter choice\n").lower()

#   computer_choices = ["rock", "paper", "scissors"]
#   computer_choice = computer_choices[randint(0, 2)]

#   print(f"CPU Chooses {computer_choice}")

#   if player_1_input == computer_choice:
#     print("The game is a time.")
#   elif player_1_input == "rock" and computer_choice == "scissors":
#     print("Player 1 wins")
#   elif player_1_input == "paper" and computer_choice == "rock":
#     print("Player 1 wins")
#   elif player_1_input == "scissors" and computer_choice == "paper":
#     print("Player 1 wins")
#   else:
#     print("CPU Wins")
# elif players == "2":
#   player_1_input = input("Player 1: Enter choice\n").lower()

#   player_2_input = input("Player 2: Enter choice\n").lower()

#   if player_1_input == player_2_input:
#     print("The game is a time.")
#   elif player_1_input == "rock" and player_2_input == "scissors":
#     print("Player 1 wins")
#   elif player_1_input == "paper" and player_2_input == "rock":
#     print("Player 1 wins")
#   elif player_1_input == "scissors" and player_2_input == "paper":
#     print("Player 1 wins")
#   else:
#     print("Player 2 wins")

