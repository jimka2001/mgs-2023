from trace import trace

@trace
def power_int(b,p):
    #print(f"--- {b}^{p}")
    if p == 0:
        return 1
    elif p == 1:
        return b
    elif p%2 == 0: # even
        return power_int(b*b, p//2)
    else: # odd
        return b * power_int(b, p-1)

print(power_int(3,3))
print(power_int(3,4))
print(power_int(2,10))
print(power_int(333,1))
print(power_int(333,0))