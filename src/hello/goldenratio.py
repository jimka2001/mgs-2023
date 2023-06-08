#send help pls

def gold_rat(x,n):
    if n == 0:
        return(x)
    else:
        y = 1 + 1/( gold_rat(x, n-1))
        print(y)
        return(y)

g = gold_rat(int(input("""
x value here
>>>""")), int(input("""
n value here
>>>""")))
print(f"The answer is {g}.")
