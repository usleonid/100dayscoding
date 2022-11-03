from art import logo
# import random
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def guess_the_number(number):
  got_it = bool()
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    number_of_attempts = EASY_LEVEL
  else:
    number_of_attempts = HARD_LEVEL
  while number_of_attempts != 0:
    print(f"You have {number_of_attempts} attempts remaining to guess the number.")
    try:
      guess = int(input("Make a guess: "))
    except:
      print("You type not a number. Please try again.")
      continue
    if guess < number:
      print("Too low.")
    elif guess > number:
      print("Too high.")
    elif guess == number:
      print(f"You got it! The answer was {number}.")
      got_it = True
      break
    number_of_attempts -= 1
    print("Guess again.")
  if got_it != True:
    print("You've run out of guesses, you lose.")


print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
secret_number = randint (1,100)
# print(f"Pssst, the correct answer is {secret_number}")

guess_the_number(secret_number)
