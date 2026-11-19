import math

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

AB = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
BC = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
AC = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

perimeter = AB + BC + AC

p = perimeter / 2
area = math.sqrt(p * (p - AB) * (p - BC) * (p - AC))

print("Сторона AB =", AB)
print("Сторона BC =", BC)
print("Сторона AC =", AC)
print("Периметр =", perimeter)
print("Площадь =", area)