x = 1.00234
# e.g., compute x**40

def slow_power(b,p):
    if p == 0:
        return 1 
    elif p == 1:
        return b
    else:
        return b * slow_power(b,p-1)

print(slow_power(2,8))

def clock_mult(x,y):
    z = (x * y) % 12
    if z == 0:
        return 12
    else:
        return z
    

#def clock_12_slow_power(b,p):
    

#print(clock_12_slow_power(9,2))

def monoid_slow_power(b,p,e,op):
    if p == 0:
        return e
    elif p == 1:
        return 
    else:
        return op(b,monoid_slow_power(b,p-1,e,op))

def concat_str(str1,str2):
    return str1 + str2


print(monoid_slow_power("hello-",6,"",concat_str))