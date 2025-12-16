a = int(input())
b = a // 100000
a = a % 100000
c = a // 10000
a = a % 10000
d = a // 1000
a = a % 1000
e = a // 100
a = a % 100
f = a // 10
a = a % 10
if b + c + d == a + e + f:
    print("YES")
else:
    print("NO")
