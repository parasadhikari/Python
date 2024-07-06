# Solve roots of a quadratic equation

# 6x**2 -17x+12=0

import cmath

##x= cmath.sqrt(100)
##print(x)
print("Enter value of a")
a=int(input())
print("Enter value of b")
b=int(input())
print("Enter value of c")
c=int(input())
d=cmath.sqrt(b**2- 4*a*c)
sol1=(-b+d)/2*a
sol2=(-b-d)/2*a
print(sol1)
print(sol2)

























