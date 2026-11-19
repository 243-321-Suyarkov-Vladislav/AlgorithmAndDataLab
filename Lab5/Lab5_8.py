N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива: ").split()))

# Чётные номера 2, 4, 6, ... → индексы 1, 3, 5, ...
min_even = a[1]
for i in range(3, N, 2):
    if a[i] < min_even:
        min_even = a[i]

print("Минимальный элемент с чётным номером =", min_even)