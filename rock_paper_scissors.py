from random import randint

print("...rock...\n...paper...\n...scissors...\n")
print("Enter 1: One Player")
print("Enter 2: Two Players")

players = input()

winning_score = int(input("What shall be the winning score?\n"))
player_1_score = 0
player_2_score = 0
cpu_score = 0

if players == "1":
  player_2 = "CPU"
else:
  player_2 = "Player 2"

if player_2 == "CPU":
  while ((player_1_score < winning_score) and (cpu_score < winning_score)):
    print("*******************************")
    print(f"Winning Score: {winning_score}\n")
    print(f"Score: Player 1 - {player_1_score} Vs. CPU - {cpu_score}")
    print("*******************************\n")

    player_1_input = input("Player 1 - Enter choice:\n").lower()

    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = computer_choices[randint(0, 2)]

    print(f"CPU Chooses {computer_choice}")

    if player_1_input == computer_choice:
      print("Tie")
    elif player_1_input == "rock" and computer_choice == "scissors":
      player_1_score += 1
      print("Player 1 wins")
    elif player_1_input == "paper" and computer_choice == "rock":
      player_1_score += 1
      print("Player 1 wins")
    elif player_1_input == "scissors" and computer_choice == "paper":
      player_1_score += 1
      print("Player 1 wins")
    else:
      cpu_score += 1
      print("CPU Wins")

  if player_1_score == winning_score:
    print(("*******************************"))
    print("Player 1 is victorious!!!")
    print(f"Final Score: Player 1 - {player_1_score} Vs. CPU - {cpu_score}")
    print(("*******************************"))
  elif cpu_score == winning_score:
    print(("*******************************"))
    print("CPU is victorious!!!")
    print(f"Final Score: Player 1 - {player_1_score} Vs. CPU - {cpu_score}")
    print(("*******************************"))
else:
  while ((player_1_score < winning_score) and (player_2_score < winning_score)):
    print("*******************************")
    print(f"Winning Score: {winning_score}\n")
    print(f"Score: Player 1 - {player_1_score} Vs. Player 2 - {player_2_score}")
    print("*******************************\n")

    player_1_input = input("Player 1: Enter choice\n").lower()
    player_2_input = input("Player 2: Enter choice\n").lower()

    if player_1_input == player_2_input:
      print("Tie")
    elif player_1_input == "rock" and player_2_input == "scissors":
      player_1_score += 1
      print("Player 1 wins")
    elif player_1_input == "paper" and player_2_input == "rock":
      player_1_score += 1
      print("Player 1 wins")
    elif player_1_input == "scissors" and player_2_input == "paper":
      player_1_score += 1
      print("Player 1 wins")
    else:
      player_2_score += 1
      print("Player 2 wins")

    if player_1_score == winning_score:
      print(("*******************************"))
      print("Player 1 is victorious!!!")
      print(f"Final Score: Player 1 - {player_1_score} Vs. Player 2 - {cpu_score}")
      print(("*******************************"))
    elif player_2_score == winning_score:
      print(("*******************************"))
      print("Player 2 is victorious!!!")
      print(f"Final Score: Player 1 - {player_1_score} Vs. Player 2 - {cpu_score}")
      print(("*******************************"))


