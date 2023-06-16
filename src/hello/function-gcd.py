count=1
def gcd(a,b):
    global count
    assert a>b, "First number has to be larger than the second number"
    assert b>0, "Neither number can be zero"
    if(a%b) == 0:
        return b
    while (a%b)!=0:
        count+=1
        return (gcd(b, a % b))
a=462846284
b=37284560
c= gcd(a,b)
print (f" The GCD of {a} and {b} is {c}.")
print(f" The number of divisions in the system was {count}.")