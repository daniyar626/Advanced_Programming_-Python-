n = int(input())
allowed = set("ABCEHKMOPTXY")
for i in range(n):
    a = str(input())
    if len(a) != 6:
        print("No")
    elif a[0] in allowed and a[4] in allowed and a[5] in allowed and a[1].isdigit()  and a[2].isdigit() and a[3].isdigit():
        print("Yes")
    else:
        print("No")
