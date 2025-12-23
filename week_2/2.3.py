a = str(input("Enter a your first number or x: "))
z = str(input("+ or -"))
b = str(input("Enter a your second number or x: "))
y = "="
c = int(input("Enter result "))
if a != "x":
    a = int(a)
elif z =="+":
    b = int(b)
    print(c - b)
elif z == "-":
    b = int(b)
    print(c + b)
if b != "x":
    b = int(b)
elif z == "+":
    a = int(a)
    print(c - a)
elif z == "-":
    a = int(a)
    print(a - c)
