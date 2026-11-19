n = int(input("Введите целое число: "))

if n == 0:
    print("нулевое число")
else:
    if n > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if n % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    print(sign, parity, "число")