import math

n = int(input("enter the smallest value "))
m = int(input("enter the largest value "))
q = math.sqrt(m)
b = math.floor(q)
print("all the prime numbers between", n, "and", m, "are:")
for num in range(n, m):
    if num > 1:
        for i in range(2, (b-3)):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
