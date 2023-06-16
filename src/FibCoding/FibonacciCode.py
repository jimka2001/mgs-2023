
n = input("Enter a n-value to calculate Fib number: ")
n = int(n)
q=0

def fib(n):
    global q
    q = q+1
    if n == 1:
        return 1
        
    elif n == 2:
        return 1 
       
    else:

        return fib(n - 2) + fib(n - 1)
print("The fibonnaci number for ", (n), " is ", fib(n))
print("The function has been called ", (q), " times!")


n = int(input("enter a limit for a taxicab number: "))






    