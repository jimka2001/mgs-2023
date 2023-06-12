n = int(input("enter the smallest value "))
m = int(input("enter the largest value "))
print("all the prime numbers between", n, "and", m, "are:")
for num in range(n, m):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
