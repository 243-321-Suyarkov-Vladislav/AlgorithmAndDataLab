P = float(input("Введите P (0 < P < 25): "))

S = 1000.0
K = 0
while S <= 1100:
    S *= 1 + P / 100
    K += 1

print("Месяцев K =", K)
print("Итоговая сумма S =", round(S, 2))