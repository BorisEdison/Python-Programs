import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[random.randint(0,len(names))]} is going to buy the meal today!")
