
def gcd(a,b):
    assert a>b, "First number has to be larger than the second number"
    assert b>0, "Neither number can be zero"
    if(a%b) == 0:
        return b
    else:
        return (gcd(b, a % b))
a=1400
b=590
c= gcd(a,b)
print (f" The GCD of {a} and {b} is {c}." )

