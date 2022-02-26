sum = 0
for n in range(1,101):
    if n%2 == 0:
        sum += n
    else:
        continue
print(sum)


sum = 0
for number in range(0,101,2):
    sum += number
print(sum)