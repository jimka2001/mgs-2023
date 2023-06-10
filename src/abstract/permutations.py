k = int(input("enter k value [number of objects selected]"))
n = int(input("enter n value [total number of objects]"))
z = int(n) - int(k)

def factorial1(n):
    if n == 0:
        return 1
    else:
        return n*(factorial1(n-1))

def factorial2(k):
    if k == 0:
        return 1
    else:
        return k*(factorial2(k-1))

def factorial3(z):
    if z == 0:
        return 1
    else:
        return z*(factorial3(z-1))
    
factorial1(n)
factorial2(k)
factorial3(z)
answer = factorial1(n)/(factorial2(k)*factorial3(z))
print(answer)