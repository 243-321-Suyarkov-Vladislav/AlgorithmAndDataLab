N = int(input("Введите N (> 2): "))
A = int(input("Введите A: "))
B = int(input("Введите B: "))

a = [A, B]
for i in range(2, N):
    a.append(sum(a))

print(a)