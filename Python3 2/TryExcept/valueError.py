try:
    x = int(input('Input an integer: '))
    print(x)
except ValueError:
    print('Value not a integer')

else:
    print('nothing went wrong')