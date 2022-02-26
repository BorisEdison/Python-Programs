
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#print(f'the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)
for _ in range(word_length):           # for _ in range(len(chosen_word)):
  display += "_"
guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter