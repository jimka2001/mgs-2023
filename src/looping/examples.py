
any(a % 3 == 1 for a in range(10))

# can use multiple lines for readablity
any(a % 3 == 1
    for a in range(10))

# (for every?) is something true for all elements in a list
all(a > 2
    for a in [2, 6, 4, 12, -34])


# find the first element which satisfies a condition


def triples(n, m):
    # find 3 cubes which sum to n
    for i in range(m):
        for a in [i, -i]:
            for j in range(i):
                for b in [-j, j]:
                    for k in range(j):
                        for c in [-k, k]:
                            if a ** 3 + b ** 3 + c ** 3 == n:
                                print(f"{n} = {a}^3 + {b}^3 + {c}^3")


#for n in range(100):
#    triples(n, 200)

def cubes(n):
    for a in range(-n,n):
        if a != 1:
            for b in range(-n,n):
                if b != 1:
                    for c in range(-n,n):
                        if c != 1:
                            if a**3 + b**3 + c**3 == 1:
                                print(f"1 = {a}^3 + {b}^3 + {c}^3")

cubes(100)
