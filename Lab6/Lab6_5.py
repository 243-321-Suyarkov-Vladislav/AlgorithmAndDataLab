M, N = 3, 4
A = [[2, 3, 1, 4], [4, 5, 3, 6], [6, 7, 5, 8]]

found = False
for j in range(N):
    all_odd = True
    for i in range(M):
        if A[i][j] % 2 == 0: # Если хотя бы один четный
            all_odd = False
            break
    
    if all_odd:
        print(f"Номер первого столбца только из нечетных: {j + 1}")
        found = True
        break

if not found:
    print(0)