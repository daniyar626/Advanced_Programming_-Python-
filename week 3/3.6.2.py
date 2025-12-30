import math
def s(a, b, e):
    p = (a + b + e) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - e))
a = int(input("1 side"))
b = int(input("2 side"))
c = int(input("3 side"))
d = int(input("4 side"))
e = int(input("diagonal"))
s1 =s(a,b,e)
s2 =s(c,d,e)
print(s1 + s2)