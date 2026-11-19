A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))

AC = abs(C - A)
BC = abs(C - B)
total = AC + BC

print("Длина отрезка AC =", AC)
print("Длина отрезка BC =", BC)
print("Сумма длин AC + BC =", total)