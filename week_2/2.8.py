a = str(input())
b = str(input())
count = 0
if len(a) != len(b):
    print("No")
for i in range(len(a)):
    c = a.count(a[i])
    d = b.count(a[i])
    if c == d:
        count = 1
    else:
        count = 0
if count == 0:
    print("No")
else:
    print("Yes")