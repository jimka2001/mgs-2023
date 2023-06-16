import math


def LDE(a, b, c, n):
    GCD = math.gcd(a, b)
    if c % GCD == 0:
        return [(x, y)
                    for x in range(n+1)
                    for y in range(n+1)
                    if a * x + b * y == c]
    else:
        print('No solution')


print(LDE(2, 4, 28, int(input('''>>>'''))))
