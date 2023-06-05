import random
# define a function which takes a single argument
greetings = ["Hello","Hi","Howdy"]
def hello(name):
    choice = random.choice(greetings)
    print(f"{choice} {user}")

# call the function with an argument
#user = input('what is your name? ')
#hello(user)
def math(num):
    print(f"The sequence is {int(num)-1}, {num}, {int(num)+1}")

math(input("enter a number "))
