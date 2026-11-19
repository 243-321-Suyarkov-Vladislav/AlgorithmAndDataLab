M, N = 3, 4
A = [[3, 9, 1, 5], [2, 8, 4, 7], [6, 0, 5, 2]]

min_val = A[0][0]
max_val = A[0][0]
min_col = 0
max_col = 0

# Ищем глобальные min/max и запоминаем индексы их столбцов
for i in range(M):
    for j in range(N):
        if A[i][j] < min_val:
            min_val = A[i][j]
            min_col = j
        if A[i][j] > max_val:
            max_val = A[i][j]
            max_col = j

# Меняем столбцы местами
for i in range(M):
    A[i][min_col], A[i][max_col] = A[i][max_col], A[i][min_col]

for row in A:
    print(row)