M, N = 3, 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [2, 2, 2, 2]]

for j in range(N):
    # Собираем элементы столбца в отдельный список
    col = [A[i][j] for i in range(M)]
    
    avg = sum(col) / M
    count = 0
    for x in col:
        if x > avg:
            count += 1
            
    print(f"В столбце {j + 1}: среднее = {avg:.2f}, элементов больше среднего = {count}")