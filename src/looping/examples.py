any(a % 3 == 1 for a in range(10))

# can use multiple lines for readablity
any(a % 3 == 1
    for a in range(10))

# (for every?) is something true for all elements in a list
all(a > 2
    for a in [2, 6, 4, 12, -34])

# find the first element which satisfies a condition
next(a
     for a in [1,2,3]
     if a * a > 100)