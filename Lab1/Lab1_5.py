a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))

ma = abs(a)
mb = abs(b)

sum_mod = ma + mb
diff_mod = ma - mb
prod_mod = ma * mb
quot_mod = ma / mb

print("Сумма модулей =", sum_mod)
print("Разность модулей =", diff_mod)
print("Произведение модулей =", prod_mod)
print("Частное модулей =", quot_mod)