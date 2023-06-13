from trace import trace


@trace
def power_int(b, p):
    if p == 0:
        return 1
    elif p == 1:
        return b
    elif p % 2 == 0:  # even
        return power_int(b * b, p // 2)
    else:  # odd
        return b * power_int(b, p - 1)


# print(power_int(3, 3))
# print(power_int(3, 4))
# print(power_int(2, 10))
# print(power_int(333, 1))
# print(power_int(333, 0))
# print(power_int(1.0123435, 100))
# print(1.0123435 ** 100)
# from math import log
#
# print(log(100, 2))

def monoid_power(b, p, e, op):
    if p == 0:
        return e
    elif p == 1:
        return b
    elif p % 2 == 0:  # even
        return monoid_power(op(b, b), p // 2, e, op)
    else:
        return op(b, monoid_power(b, p - 1, e, op))


@trace
def float_mult(a, b):
    return a * b


print(monoid_power(1.012, 255, 1.0, float_mult))
