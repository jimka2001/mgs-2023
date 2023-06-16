
print(any(x % 2 for x in range(6)))
print(not any(x % 2 for x in range(6)))
print(all(x % 2 != 0 for x in range(6)))
print('''
''')
print(all(x % 2 for x in range(6)))
print(not all(x % 2 == 0 for x in range(6)))
print(any(x % 2 != 0 for x in range(6)))

print(any(all (y % 2 == 0
            for y in range(x))
        for x in range(10)))

print([x*x for x in range(10) if x % 2 ==0])

print([x*y
        for x in range(10)
        for y in range(10) if x % 2 == 0 or y % 2 == 0])

print([(x,y, x*x+y*y)
        for x in range(10) 
        for y in range(10)
        if (x*x + y*y) % 3 == 0])

for x in range(100):
    for y in range(200):
        if (x*x+y*y) % 3 == 0:
            print((x,y,x*x+y*y))
print({x*y
            for x in range(10)
            for y in range(10)
            if (x*y) % 2})