N = int(input("Введите N (> 0): "))

product = 1.0
for i in range(1, N + 1):
    factor = 1 + i / 10
    product *= factor

print("Произведение =", product)