A = float(input("Введите A: "))
B = float(input("Введите B (A > B): "))

remainder = A
while remainder >= B:
    remainder -= B

print("Длина незанятой части =", round(remainder, 10))