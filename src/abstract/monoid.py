items = ("e", "a", "b")

def is_associative(op):
    return all(op(op(a, b), c) == op(a, op(b, c))
               for a in items
               for b in items
               for c in items)

def is_abelian(op):
    return all(op(x,y) == op(y,x)
               for x in items
               for y in items
               )


def op1(x,y):
    assert x in items
    assert y in items
    if x == "e":
        return y
    elif y == "e":
        return x
    else:
        return "a"

def op2(x,y):
    if x == "e":
        return y
    elif y == "e":
        return x
    else:
        return x

def op3(x,y):
    if x == "e":
        return y
    elif y == "e":
        return x
    elif x == "a":
        return y
    else:
        return "a"

print(is_abelian(op2))

