import math
def gip(a, b):
    return math.sqrt(a**2 + b**2)
a = int(input("first katet"))
b = int(input("second katet"))
g = gip(a, b)
print("first hypotenuse is", g)
c = int(input("third katet"))
d = int(input("fourth katet"))
f = gip(c, d)
print("second hypotenuse is", f)
if g > f:
    print("first hypotenuse is greater", g - f)
elif g < f:
    print("second hypotenuse is greater", f - g)
elif g == f:
    print("hypotenuse is equal")