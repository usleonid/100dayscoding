from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, alphabet, direction):
  new_text = str()
  if shift >= 25:
    shift = shift % 25
  for symbol in text:
    try:
      symbol_index = alphabet.index(symbol)
      if direction == 'encode':
        if (symbol_index + shift) <= 25:
          new_text += alphabet[symbol_index+shift]
        else:
          new_text += alphabet[shift - (25 - symbol_index)]
      elif direction == 'decode':
        if (symbol_index - shift) >= 0:
          new_text += alphabet[symbol_index-shift]
        else:
          new_text += alphabet[25 - (shift - symbol_index)]
    except:
      new_text += symbol
  print(f"\nThe {direction}d result:\n{new_text}")

while True:
  direction = input("\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))

  caesar(text = text, shift = shift, alphabet = alphabet, direction = direction)
  go_again = input('\nDo you want to restart the cipher program? Please, type "Yes" or "No"\n').lower()
  if go_again == 'yes':
    continue
  else:
    print('\nThank you! Bye!')
    break



# def encrypt(text, shift, alphabet):
#   new_text = str()
#   for symbol in text:
#     try:
#       symbol_index = alphabet.index(symbol)
#       if (symbol_index + shift) <= 25:
#         new_text += alphabet[symbol_index+shift]
#       else:
#         new_text += alphabet[shift - (25 - symbol_index)]
#     except:
#       new_text += symbol
#   print(new_text)

# def decrypt(text, shift, alphabet):
#   new_text = str()
#   for symbol in text:
#     try:
#       symbol_index = alphabet.index(symbol)
#       if (symbol_index - shift) >= 0:
#         new_text += alphabet[symbol_index-shift]
#       else:
#         new_text += alphabet[25 - (shift - symbol_index)]
#     except:
#       new_text += symbol
#   print(new_text)

# def caesar(direction):
#   if direction == 'encode':
#     encrypt(text = text, shift = shift, alphabet = alphabet)
#   elif direction == 'decode':
#     decrypt(text = text, shift = shift, alphabet = alphabet)
