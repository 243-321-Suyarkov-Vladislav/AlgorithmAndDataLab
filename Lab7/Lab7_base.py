def bubble_sort(arr):
    n = len(arr)
    # Внешний цикл: количество проходов
    for i in range(n):
        # Внутренний цикл: сравнение пар соседних элементов
        # n - i - 1, потому что после i-го прохода i элементов в конце уже отсортированы
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего — меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Проверка работы
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Отсортированный массив:", sorted_numbers)