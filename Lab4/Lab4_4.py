def is_palindrome(s):
    s = s.lower().replace(" ", "")  # приводим к нижнему регистру и убираем пробелы
    if len(s) <= 1:                 # базовый случай
        return True
    if s[0] != s[-1]:               # крайние символы не совпали
        return False
    return is_palindrome(s[1:-1])   # рекурсивный случай: отбрасываем крайние символы

text = input("Введите строку: ")
print(is_palindrome(text))