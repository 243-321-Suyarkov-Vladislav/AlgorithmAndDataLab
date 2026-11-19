N = int(input("Введите N (> 1): "))
A = float(input("Введите первый член A: "))
D = float(input("Введите знаменатель D: "))

a = []
current = A
for i in range(N):
    a.append(current)
    current *= D

print(a)