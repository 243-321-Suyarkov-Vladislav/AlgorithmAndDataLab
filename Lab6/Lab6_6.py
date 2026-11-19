M, N = 3, 4
A = [[3, 8, 1, 5], [9, 2, 7, 4], [6, 0, 8, 2]]

for i in range(M):
    row = A[i]
    # Находим индексы минимума и максимума в строке
    min_idx = row.index(min(row))
    max_idx = row.index(max(row))
    
    # Меняем местами
    row[min_idx], row[max_idx] = row[max_idx], row[min_idx]

for row in A:
    print(row)