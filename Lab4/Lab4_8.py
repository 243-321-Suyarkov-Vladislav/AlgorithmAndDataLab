def count_digits(n):
    n = abs(n)              # работаем с модулем числа
    if n < 10:              # базовый случай: одна цифра
        return 1
    return 1 + count_digits(n // 10)  # отбрасываем последнюю цифру

n = int(input("Введите число: "))
print("Количество цифр:", count_digits(n))