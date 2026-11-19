import math

xa = float(input("x точки A: "))
ya = float(input("y точки A: "))
xb = float(input("x точки B: "))
yb = float(input("y точки B: "))
xc = float(input("x точки C: "))
yc = float(input("y точки C: "))

AB = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
AC = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)

if AB < AC:
    print("Ближе точка B, расстояние =", AB)
elif AC < AB:
    print("Ближе точка C, расстояние =", AC)
else:
    print("Точки B и C на одинаковом расстоянии =", AB)