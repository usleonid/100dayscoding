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

#Write your code below this line 👇

print ("Welcome to 'Rock, Paper, Scissors' game!")
game_choice = [rock, paper, scissors]
while True:
  user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")

  # if user_choice == "0":
  #   print(rock)
  # elif user_choice == "1":
  #   print(paper)
  # else:
  #   print(scissors)
  if int(user_choice) >= 3 or int(user_choice) < 0:
      print("You have typed incorrect number. Please try again!")
      continue
  else:
      print(game_choice[int(user_choice)])

      comp_choice = random.randint(0,2)

      print("\nComputer choice:")

      # if comp_choice == 0:
      #   print(rock)
      # elif comp_choice == 1:
      #   print(paper)
      # else:
      #   print(scissors)

      print(game_choice[comp_choice])

      if comp_choice == 0 and user_choice == "1":
        print ("\nYou win!:)")
        break
      elif comp_choice == 0 and user_choice == "2":
        print ("\nYou lose!:(")
        break
      elif comp_choice == 1 and user_choice == "0":
        print ("\nYou lose!:(")
        break
      elif comp_choice == 1 and user_choice == "2":
        print("\nYou win!:)")
        break
      elif comp_choice == 2 and user_choice == "0":
        print("\nYou win!:)")
        break
      elif comp_choice == 2 and user_choice == "1":
        print("\nYou lose!:(")
        break
      else:
        print("Draw! Please try again.")
        continue
