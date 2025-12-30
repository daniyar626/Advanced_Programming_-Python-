a = list(map(int, input("Введите элементы: ").split()))
b = list(map(int, input("Введите элементы: ").split()))
c = list(map(int, input("Введите элементы: ").split()))

d = sum(a) / len(a)
e = sum(b) / len(b)
f = sum(c) / len(c)

print("sum of the elements and the arithmetic mean", sum(a), d)
print("sum of the elements and the arithmetic mean", sum(b), e)
print("sum of the elements and the arithmetic mean", sum(c), f)
