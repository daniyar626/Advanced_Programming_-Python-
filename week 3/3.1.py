import math
def rec(a, b):
    return a * b
def tri(c, d):
   return 0.5*c*d
def cir(r):
    return math.pi * r * r
a = float(input("Введите сторону прямоугольника a: "))
b = float(input("Введите сторону прямоугольника b: "))
print("Площадь прямоугольника:", rec(a, b))

c = float(input("Введите основание треугольника: "))
d = float(input("Введите высоту треугольника: "))
print("Площадь треугольника:", tri(c, d))

r = float(input("Введите радиус круга: "))
print("Площадь круга:", cir(r))

