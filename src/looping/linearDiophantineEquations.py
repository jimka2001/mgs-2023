import math
def LDE(a,b,c,n):
    GCD = math.gcd(a,b)
    if c % GCD == 0:
        return(any(print((x,y))
        for x in range(n)
        for y in range(n)
        if a * x + b *y == c))
    else:
        print('No solution')
LDE(10,15,55,int(input('''>>>''')))
