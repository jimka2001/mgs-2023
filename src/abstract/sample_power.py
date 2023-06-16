from trace import trace

x = 1.00234
# e.g., compute x**40

@trace
def int_slow_power(b,p):
    if p==0:
        return 1
    elif p==1:
        return b
    else:
        return b * int_slow_power(b, p-1)


def str_slow_power(b,p):
    if p==0:
        return ""
    elif p==1:
        return b
    else:
        return b + str_slow_power(b, p-1)

def clock_mult(x,y):
    z = (x*y)  % 12
    if z == 0:
        return 12
    else:
        return z

def clock_11_mult(x,y):
    z = (x*y)  % 11
    return z

def clock_12_slow_power(b,p):
    if p==0:
        return 1
    elif p==1:
        return b
    else:
        return clock_mult(b,clock_12_slow_power(b, p-1)) 

#print(clock_12_slow_power(7,51))

@trace
def monoid_slow_power(b,p,e,op):
    if p==0:
        return e
    elif p==1:
        return b
    else:
        return op(b,monoid_slow_power(b, p-1, e ,op)) 

def concat_str(str1,str2):
    return str1 + str2

print(monoid_slow_power("hello-",6,"",concat_str))
print(monoid_slow_power(3,51,1,clock_mult))
print("------------------------------------------")

def monoid_fast_power(b,p,e,op):
    if p==0:
        return e
    elif p==1:
        return b
    elif p%2 == 0:
        return monoid_fast_power(op(b,b), p//2,e, op)
    else:  # odd
        return op(b, monoid_fast_power(b, p-1, e, op))

print(monoid_fast_power("hello-",6,"",concat_str))
print(monoid_fast_power(3,256,1,clock_mult))
print(monoid_fast_power(3,256,1,clock_mult))
print(monoid_fast_power(3,13,1,clock_11_mult))
print("--------------------")
for p in range(12):
    print(monoid_fast_power(3,p,1,clock_11_mult))