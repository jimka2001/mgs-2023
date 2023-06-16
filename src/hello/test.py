def gold_rat(x,n):
    if n == 0:
        return(x)
    else:
        return(1+(1 / gold_rat(x,n-1)))
        
g = gold_rat(int(input("""
x value here
>>>""")), int(input("""
n value here
>>>""")))
print(f"The answer is {g}.")