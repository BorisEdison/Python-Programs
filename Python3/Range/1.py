#For Loop with Range
for number in range(1, 11):   #prints 1-10
    print(number)

for number in range(1, 11, 3): #prints 1 4 7 10
    print(number)

total = 0
for number in range(1,101):
    total += number
print(total)