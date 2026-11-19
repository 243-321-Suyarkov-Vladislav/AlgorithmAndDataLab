def factorial(n):
    if n == 0 or n == 1:      # базовый случай
        return 1
    return n * factorial(n - 1)  # рекурсивный случай

n = int(input("Введите n: "))
print("n! =", factorial(n))