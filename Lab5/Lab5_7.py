N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива: ").split()))

d = a[1] - a[0]
is_progression = True

for i in range(2, N):
    if a[i] - a[i - 1] != d:
        is_progression = False
        break

if is_progression:
    print("Разность прогрессии =", d)
else:
    print(0)