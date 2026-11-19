def power(x, n):
    if n == 0:              # базовый случай: x^0 = 1
        return 1
    if n < 0:               # отрицательная степень
        return 1 / power(x, -n)
    return x * power(x, n - 1)  # рекурсивный случай

x = float(input("Введите x: "))
n = int(input("Введите n: "))
print("x^n =", power(x, n))