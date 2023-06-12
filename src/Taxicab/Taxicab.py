
# def taxi(t):
# global a
# global b
# [a+b for a in range(int(cb))
#  for b in range(int())
#   if a+b % 2 == 0]
#
#  [a+b for a in range(int(-cb))
#   for b in range(int(-cb))
#    if a+b % 2 == 0]


# print(taxi(t), a, b)


n = int(input("enter a limit for a taxicab number: "))

print(
{(a,b,c,d)
 for a in range(-n,n)
 for b in range(-n,n)
  for c in range(-n,n)
   for d in range(-n,n)
 if a**(3)+b**(3) == c**(3)+d**(3)
 if a!=c and b!=d and a!=b and b!=c and d!=a and a!=-c and b!=-d and a!=-b and b!=-c and d!=-a}
)

