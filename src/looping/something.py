import math
def LDE(a,b,c):
    GCD = math.gcd(a,b)
    if c % GCD == 0:
        return(any(print((x,y))
        for x in range(10000000000)
        for y in range(10000000000)
        if a * x + b *y == c))
    else:
        print('No solution')
LDE(10,15,55)
