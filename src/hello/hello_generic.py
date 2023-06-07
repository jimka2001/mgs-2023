# define a function which takes a single argument
def hello(first, last):
    print("hello, " + first + " " + last)

# call the function with an argument
hello(input("""
First Name
>>>"""), input("""
Last Name
>>>"""))


