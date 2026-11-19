def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def decompose(n, start=None):
    if n == 0:                  # базовый случай: разложение найдено
        return []
    if n == 1:                  # единицу простыми числами не набрать
        return None
    if start is None:
        start = n

    for p in range(start, 1, -1):    # перебираем простые числа не больше n
        if is_prime(p) and p <= n:
            rest = decompose(n - p, p)  # рекурсивно раскладываем остаток
            if rest is not None:
                return [p] + rest

    return None

n = int(input("Введите число: "))
result = decompose(n)
print("Разложение:", result)