def fib(n):
    if n <= 1:          # базовый случай: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)  # рекурсивный случай

n = int(input("Введите n: "))
print("fib(n) =", fib(n))