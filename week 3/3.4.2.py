def rad(x, y, a, b, r):
    return (x-a)**2 + (y-b)**2 <= r**2
a = int(input())
b = int(input())
r = int(input())
p1 = int(input())
p2 = int(input())
f1 = int(input())
f2 = int(input())
l1 = int(input())
l2 = int(input())
count = 0
if rad(p1, p2, a, b, r):
    count = count + 1
if rad(f1, f2, a, b, r):
    count = count + 1

if rad(l1, l2, a, b, r):
    count = count + 1
