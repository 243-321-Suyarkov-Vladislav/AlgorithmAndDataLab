M, N = 3, 4
A = [[2, 3, 1, 4], [1, 2, 3, 4], [5, 1, 2, 3]]

min_prod = float('inf')
min_col_index = 0

for j in range(N):
    prod = 1
    for i in range(M):
        prod *= A[i][j]
    
    if prod < min_prod:
        min_prod = prod
        min_col_index = j + 1 # Номер столбца (с 1)

print(f"Номер столбца: {min_col_index}")
print(f"Наименьшее произведение: {min_prod}")