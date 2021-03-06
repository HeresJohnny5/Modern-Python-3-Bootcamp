from random import randint
cpu_random_num = randint(1, 10)

keep_playing = True
user_input = None

while keep_playing: 
  while user_input != cpu_random_num:
    user_input = int(input("Guess a number between 1 and 10:\n"))

    if user_input < cpu_random_num:
      print("Too low, try again!")
    else:
      print("Too high, try again!")

  print("CONGRATS! You guessed correctly!")

  keep_playing = input("Do you want to keep playing? (y/n)\n")

  if keep_playing == "y":
    cpu_random_num = randint(1, 10)
    user_input = int(input("Guess a number between 1 and 10:\n"))
  else:
    print("Thanks for playing! Bye!")
    keep_playing = False
