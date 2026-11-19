def binary_search_visual(arr, target):
    print(f"Ищем число {target} в массиве: {arr}\n")
    left = 0
    right = len(arr) - 1
    step = 1

    while left <= right:
        mid = (left + right) // 2
        print(f"--- Шаг {step} ---")
        print(f"Границы: left={left}, right={right}. Середина mid={mid} (значение {arr[mid]})")

        if arr[mid] == target:
            print(f"УСПЕХ! Значение {target} найдено по индексу {mid}.")
            return mid
        elif arr[mid] > target:
            print(f"{arr[mid]} > {target}. Ищем в левой половине. Сдвигаем right на {mid - 1}.")
            right = mid - 1
        else:
            print(f"{arr[mid]} < {target}. Ищем в правой половине. Сдвигаем left на {mid + 1}.")
            left = mid + 1
        step += 1
        print()

    print("Элемент не найден. Границы пересеклись (left > right).")
    return -1

numbers = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
binary_search_visual(numbers, 36)