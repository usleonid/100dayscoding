import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
# word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 7
attempt = 0

print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = list()
for _ in chosen_word:
  display.append('_')
# print(display)
print(f"\nTry to guess the word \n{' '.join(display)}\n")

while display.count('_') > 0 or lives > 0:

  attempt += 1
  print(f"\nAttempt No. {attempt}")
  guess = input("Guess a letter: ").lower()
  clear()

  for position in range(len(chosen_word)):
      if chosen_word[position] == guess:
        display[position] = chosen_word[position]
  if guess not in display:
      lives -= 1
      print(f"You guessed {guess}, that's not in the word. \nYou lose a life: \n{stages[lives]}")

  print(f"{' '.join(display)}")

  if lives == 0:
    print('\nYou lose!')
    break
  elif '_' not in display:
    print('\nYou win!\n')
    break
