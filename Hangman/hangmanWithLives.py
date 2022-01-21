import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
#print(f'The solution is {chosen_word}.')

display = []
for _ in range(word_length):    #Create blanks
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):  #Check guessed letter     #range(0,word_length)
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
    lives = lives - 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  print(f"{' '.join(display)}")  #Join all the elements in the list and turn it into a String.

  if "_" not in display:       #Check if user has got all letters.
      end_of_game = True
      print("You win.")
  
  print(stages[6-lives])