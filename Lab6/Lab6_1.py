M = int(input("Введите нечетное M: "))

# Заполнение матрицы числами по порядку (от 1 до M*M)
A = [[i * M + j + 1 for j in range(M)] for i in range(M)]

# Вывод исходной матрицы, чтобы легко сверить результат
print("\nИсходная матрица:")
for row in A:
    print(*row, sep="\t")

top, bottom = 0, M - 1
left, right = 0, M - 1

print("\nЭлементы по спирали:")
while top <= bottom and left <= right:
    # 1. Первый столбец (сверху вниз)
    for i in range(top, bottom + 1):
        print(A[i][left], end=" ")
    left += 1

    # 2. Последняя строка (слева направо)
    if top <= bottom:
        for j in range(left, right + 1):
            print(A[bottom][j], end=" ")
        bottom -= 1

    # 3. Последний столбец (снизу вверх)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(A[i][right], end=" ")
        right -= 1

    # 4. Первая строка (справа налево)
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(A[top][j], end=" ")
        top += 1