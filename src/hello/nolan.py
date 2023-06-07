#define a function which takes a single argument
#def hello(name):
    #print("hello " + name)

#call the function with an argument
#hello("gertrude")

def factorial(n):
    assert n>=0, f"cannot compute factorial of {n} "
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))