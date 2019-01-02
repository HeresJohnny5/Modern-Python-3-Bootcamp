from random import randint

def game_start():
  print("...rock...\n...paper...\n...scissors...\n")
  print("Enter 1: One Player")
  print("Enter 2: Two Players")

  players = input()
  player_2 = None

  winning_score = int(input("What shall be the winning score?\n"))
  player_1_score = 0
  player_2_score = 0

  if players == "1":
    player_2 = "CPU"
    one_player(winning_score, player_1_score, player_2, player_2_score)
  else:
    player_2 = "Player 2"
    two_players(winning_score, player_1_score, player_2, player_2_score)

def game_header(winning_score, player_1_score, player_2, player_2_score):
  print("*******************************")
  print(f"Winning Score: {winning_score}\n")
  print(f"Score: Player 1 - {player_1_score} Vs. {player_2} - {player_2_score}")
  print("*******************************\n")

def game_logic(player_1_input, player_1_score, player_2_input, player_2_score, player_2):
  score = { "player_1_score": None, "player_2_score": None }

  if player_1_input == player_2_input:
    print("Tie")
    score["player_1_score"] = player_1_score
    return score
  elif player_1_input == "rock" and player_2_input == "scissors":
    player_1_score += 1
    print("Player 1 wins")
    score["player_1_score"] = player_1_score
    return score
  elif player_1_input == "paper" and player_2_input == "rock":
    player_1_score += 1
    print("Player 1 wins")
    score["player_1_score"] = player_1_score
    return score
  elif player_1_input == "scissors" and player_2_input == "paper":
    player_1_score += 1
    print("Player 1 wins")
    score["player_1_score"] = player_1_score
    return score
  else:
    player_2_score += 1
    print(f"{player_2} Wins")
    score["player_2_score"] = player_2_score
    return score

def winner(player_1_score, player_2, player_2_score, winning_score):
  if player_1_score == winning_score:
    print(("*******************************"))
    print("Player 1 is victorious!!!")
    print(f"Final Score: Player 1 - {player_1_score} Vs. {player_2} - {player_2_score}")
    print(("*******************************"))
  elif player_2_score == winning_score:
    print(("*******************************"))
    print("CPU is victorious!!!")
    print(f"Final Score: Player 1 - {player_1_score} Vs. {player_2} - {player_2_score}")
    print(("*******************************"))

def one_player(winning_score, player_1_score, player_2, player_2_score):
  while ((player_1_score < winning_score) and (player_2_score < winning_score)):
    game_header(winning_score, player_1_score, player_2, player_2_score)

    player_1_input = input("Player 1 - Enter choice:\n").lower()

    computer_choices = ["rock", "paper", "scissors"]
    player_2_input = computer_choices[randint(0, 2)]

    print(f"CPU Chooses {player_2_input}")

    score_dictionary = game_logic(player_1_input, player_1_score, player_2_input, player_2_score, player_2)

    if type(score_dictionary["player_1_score"]) == int:
      player_1_score = score_dictionary["player_1_score"]
    elif type(score_dictionary["player_2_score"]) == int:
      player_2_score = score_dictionary["player_2_score"]
    else:
      game_logic(player_1_input, player_1_score, player_2_input, player_2_score, player_2)

  winner(player_1_score, player_2, player_2_score, winning_score)

def two_players(winning_score, player_1_score, player_2, player_2_score):
  while ((player_1_score < winning_score) and (player_2_score < winning_score)):
    game_header(winning_score, player_1_score, player_2, player_2_score)

    player_1_input = input("Player 1: Enter choice\n").lower()
    player_2_input = input("Player 2: Enter choice\n").lower()

    score_dictionary = game_logic(player_1_input, player_1_score, player_2_input, player_2_score, player_2)

    if type(score_dictionary["player_1_score"]) == int:
      player_1_score = score_dictionary["player_1_score"]
    elif type(score_dictionary["player_2_score"]) == int:
      player_2_score = score_dictionary["player_2_score"]
    else:
      game_logic(player_1_input, player_1_score, player_2_input, player_2_score, player_2)

  winner(player_1_score, player_2, player_2_score, winning_score)
    
game_start()