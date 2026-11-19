N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива: ").split()))

last_index = -1
for i in range(1, N - 1):          # крайние элементы не могут быть локальными максимумами
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        last_index = i

if last_index == -1:
    print("Локальных максимумов нет")
else:
    print("Номер последнего локального максимума =", last_index + 1)