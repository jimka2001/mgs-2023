from math import sqrt

def testRoots():
    assert roots(1,0,0) == {0}
    assert roots(3,6,3) == {-1}
    assert roots(1,13,12) == {-1, -12}
    assert roots(1,-1,-12) == {4, -3}
    assert roots(1,3,-10) == {2, -5}
    assert roots(1,2,2) == {}

#testRoots()


def roots(a, b, c):
    disc = b*b - 4*a*c
    if disc < 0:
        return {}
    else:    
        r= {(-b + sqrt(disc))/(2*a),
            (-b - sqrt(disc))/(2*a)}
        print(r)
        return r


print("Enter the following values for your quadratic")
a = int(input("A value: "))
b = int(input("B value: "))
c = int(input("C value: "))
roots(a,b,c)

#assert roots(1,13,12) == {-1,-12}

