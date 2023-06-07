k = int(input("enter k value [number of objects selected]"))
n = int(input("enter n value [total number of objects]"))

def choose(n,k):
    if k==1:
        return n
    else:
        return (n/k)*choose(n-1, k-1)

answer = choose(n,k)
print(answer)