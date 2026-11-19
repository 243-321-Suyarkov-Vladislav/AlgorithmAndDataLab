N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))

result = []

# Нечётные номера (1, 3, 5, ...) — это индексы 0, 2, 4, ...
for i in range(0, N, 2):
    result.append(a[i])

# Чётные номера (N или N-1, ... , 2) — это индексы N-1 или N-2, ... , 1
start = N - 1 if (N - 1) % 2 == 1 else N - 2
for i in range(start, 0, -2):
    result.append(a[i])

print(result)