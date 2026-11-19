n = int(input("Введите число от 1 до 999: "))

if n % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

if n < 10:
    digits = "однозначное"
elif n < 100:
    digits = "двузначное"
else:
    digits = "трехзначное"

print(parity, digits, "число")