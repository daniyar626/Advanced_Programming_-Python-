a = str(input())
b= str(input())
count = 0
n = len(b)
c = b + b
for i in range(len(a) + 1 -n ):
    d = a[i : i+n]
    if d in c:
        count += 1
print(count)
