A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A != B:
    if A > B:
        B = A
    else:
        A = B
else:
    A = 0
    B = 0

print("A =", A)
print("B =", B)