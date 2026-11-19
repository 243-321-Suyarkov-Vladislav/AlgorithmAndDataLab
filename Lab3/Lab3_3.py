N = int(input("Введите N (> 0): "))

total = 0
for i in range(1, N + 1):
    total += 2 * i - 1
    print("После добавления", 2 * i - 1, "сумма =", total)

print("Квадрат числа", N, "равен", total)