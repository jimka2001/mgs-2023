from math import sqrt

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
