N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива: ").split()))
K = int(input("Введите K: "))
L = int(input("Введите L: "))

total = 0
count = 0
for i in range(K - 1, L):   # номера K..L → индексы K-1..L-1
    total += a[i]
    count += 1

average = total / count
print("Среднее арифметическое =", average)