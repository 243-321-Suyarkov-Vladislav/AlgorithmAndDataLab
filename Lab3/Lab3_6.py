A = int(input("Введите A: "))
B = int(input("Введите B (A < B): "))

for num in range(A, B + 1):
    for _ in range(num):
        print(num, end=" ")
    print()