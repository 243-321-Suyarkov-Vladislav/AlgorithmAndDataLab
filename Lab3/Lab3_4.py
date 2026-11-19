A = float(input("Введите A: "))
N = int(input("Введите N (> 0): "))

total = 0
power = 1
for i in range(N + 1):
    total += power
    power *= A

print("Сумма =", total)