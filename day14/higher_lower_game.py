from art import logo, vs
from game_data import data
from replit import clear
from random import randint

def data_for_compare(list_of_data):
    card_on_hand = data[randint(0,len(list_of_data)-1)]
    return card_on_hand

def user_choosing(compared_a, compared_b):
  while True:
    user_choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
      user_choice = compared_a
      break
    elif user_choice == 'b':
      user_choice = compared_b
      break
    else:
      print("You choose undefined value. Please try again!")
      continue
  return user_choice

def check_right_answer(compared_a, compared_b):
  if compared_a['follower_count'] > compared_b['follower_count']:
    right_answer = compared_a['follower_count']
  elif compared_b['follower_count'] > compared_a['follower_count']:
    right_answer = compared_b['follower_count']
  else:
    right_answer = user_choosing(compared_a, compared_b)['follower_count']
  return right_answer

score = 0

a = data_for_compare(data)
print(logo)

while True:

  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")

  print(vs)

  b = a
  while b == a:
    b = data_for_compare(data)
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

  user = user_choosing(a,b)
  right = check_right_answer(a,b)
  if user['follower_count'] == right:
    a = b
    score += 1
    clear()
    print(logo+f"\nYou're right! Current score: {score}.")
  else:
    clear()
    print(logo+f"\nSorry, that's wrong. Final score: {score}")
    break
