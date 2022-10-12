#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = str()

# letter_part = str()

for i in range(nr_letters):
  # letter_part += random.choice(letters)
  password += random.choice(letters)
# print(letter_part)

# symbol_part = str()

for i in range(nr_symbols):
  # symbol_part += random.choice(symbols)
  password += random.choice(symbols)
# print(symbol_part)

# number_part = str()

for i in range(nr_numbers):
  # number_part += random.choice(numbers)
  password += random.choice(numbers)
# print(number_part)

# password_shufle = random.shuffle(password)

print("Here is your password: "+password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

# letter_part = str()

for i in range(nr_letters):
  # letter_part += random.choice(letters)
  password.append(random.choice(letters))
# print(letter_part)

# symbol_part = str()

for i in range(nr_symbols):
  # symbol_part += random.choice(symbols)
  password.append(random.choice(symbols))
# print(symbol_part)

# number_part = str()

for i in range(nr_numbers):
  # number_part += random.choice(numbers)
  password.append(random.choice(numbers))
# print(number_part)

random.shuffle(password)
final_pas = str()

for symbol in password:
  final_pas += symbol

print("Here is your password: "+final_pas)
