
n = input("Enter a n-value to calculate Fib number: ")
n = int(n)
x = float(5**0.5)
def fibcalc(n):
    return ((((1+x)/2)**n)-(((1-x)/2)**n))/(x)

print("The fibonnaci number for ", (n), " is ", round(fibcalc(n)), "!")






    