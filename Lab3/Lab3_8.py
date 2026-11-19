N = int(input("Введите N (> 1): "))

total = 0
K = 0
while total < N:
    K += 1
    total += K

print("K =", K)
print("Сумма =", total)