N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива: ").split()))

positions = []
for i in range(N):
    for j in range(i + 1, N):
        if a[i] == a[j]:
            positions = [i + 1, j + 1]

print("Номера одинаковых элементов:", positions)