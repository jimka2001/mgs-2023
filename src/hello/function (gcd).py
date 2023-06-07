
def gcd(a,b):
    assert a>b, "First number has to be larger than the second number"
    assert b>0, "Neither number can be zero"
    if(a%b) == 0:
        return b
    else:
        return (gcd(b, a % b))
a=43830
b=690
c= gcd(a,b)
print (f" The GCD of {a} and {b} is {c}.")


