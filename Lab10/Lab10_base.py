def binary_search(arr, target):
    # 1. Устанавливаем начальные границы
    left = 0
    right = len(arr) - 1

    # 2. Пока левая граница не пересекла правую
    while left <= right:
        # a. Находим середину
        mid = (left + right) // 2

        # b. Если нашли — возвращаем индекс
        if arr[mid] == target:
            return mid
        
        # c. Если средний больше искомого — ищем в левой половине
        elif arr[mid] > target:
            right = mid - 1
            
        # d. Если средний меньше искомого — ищем в правой половине
        else:
            left = mid + 1

    # 3. Если цикл закончился, а элемент не найден
    return -1

# Проверка работы
numbers = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
target = 36
result = binary_search(numbers, target)

if result != -1:
    print(f"Элемент {target} найден по индексу {result}")
else:
    print("Элемент не найден")