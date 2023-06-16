print(any(x%2==0 for x in [40,100,2]))
print(not any(x%2==0 for x in range (40,100,2)))
print(all(not x%2 == 0 for x in range(40,100,2)))
print("-----------------------------------------")
print(all(x%2==0 for x in [1,2,3,4,5]))
print(not all(x%2==0 for x in [1,2,3,4,5]))
print(any(x%2 != 0 for x in [1,2,3,4,5]))

print({x*x for x in range(0,10,2)})


for x in range(100):
    for y in range(200):
        if (x*x+y*y) % 3== 0:
            print((x,y,x*y+y*y))


print({(x*y)
        for x in range(10)
        for y in range(10)
        if (x*y) %2 == 0})
