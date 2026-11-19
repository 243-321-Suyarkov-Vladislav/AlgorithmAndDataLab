M, N = 3, 4
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
K = int(input("Введите K: "))

row = A[K - 1] # Индексы в Python начинаются с 0

sum_row = sum(row)
prod_row = 1
for x in row:
    prod_row *= x

print(f"Сумма элементов {K}-й строки: {sum_row}")
print(f"Произведение элементов {K}-й строки: {prod_row}")