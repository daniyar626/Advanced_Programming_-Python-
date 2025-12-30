def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input())
b = int(input())
c = int(input())
d = int(input())
up = a * d
low = b * c
f = gcd(up, low)
up = up // f
low = low // f
print(up, "/", low)
