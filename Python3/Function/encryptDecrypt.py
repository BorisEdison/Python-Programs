alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

cipher_text = []
plain_text = []

#Encrypt function
def encrypt(plain_text, shift_amount):
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if (new_position > 25):
      new_position -= 26
    new_letter = alphabet[new_position]
    cipher_text.append(new_letter)

  print(f"The encoded text is {''.join(cipher_text)}")

#Decrypt function
def decrypt(cipher_text,shift_amount):
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text.append(alphabet[new_position])
  
  print(f"The decoded text is {''.join(plain_text)}")

if (direction == "encode"):
 encrypt(plain_text = text, shift_amount = shift)
elif (direction == "decode"):
  decrypt(cipher_text = text, shift_amount = shift)