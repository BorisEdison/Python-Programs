def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?")

greet()

def greet_with_name(name):   # parameter(name): parameter is the name of the argument that is passed in
  print(f"Hello {name}")
  print(f"How do you do {name}?")


greet_with_name("Boris")    #argument: actual value of the data