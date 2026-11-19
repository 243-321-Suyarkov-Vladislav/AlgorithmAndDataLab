M, N = 4, 4
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]

half_M = M // 2
half_N = N // 2

for i in range(half_M):
    for j in range(half_N):
        # Меняем элемент из левой верхней четверти 
        # с соответствующим из правой нижней
        A[i][j], A[i + half_M][j + half_N] = A[i + half_M][j + half_N], A[i][j]

for row in A:
    print(row)