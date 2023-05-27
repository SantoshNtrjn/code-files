import string
alphabet = list(string.ascii_lowercase)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    elif char in alphabet:
      position = alphabet.index(char)
      new_position = (position + shift_amount)%26
      end_text += alphabet[new_position]
    
  print(f"\nHere's the {cipher_direction}d result: {end_text}")

import art
print(art.logo)

start = False

while not start:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  question = input("\nDo you wanna go again? (yes/no):: ").lower()
  if question == "no":
    print("\nBye!")
    start = True