from math import sqrt

def roots(a, b, c):
    return ((-b + sqrt(b*b - 4*a*c))/(2*a),
            (-b - sqrt(b*b - 4*a*c)/(2*a)))

def testRoots():
    print(roots(1, 0, 0))
    assert roots(1,0,0) == (0,0)