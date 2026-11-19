def insertion_sort_visual(arr):
    print("Начальный массив:", arr)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\n--- Шаг {i}: Берем элемент {key} ---")
        
        # Сдвигаем элементы
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(f"Сдвигаем {arr[j]} вправо: {arr}")
            j -= 1
            
        # Вставляем
        arr[j + 1] = key
        print(f"Вставляем {key} на позицию {j + 1}: {arr}")

    return arr

numbers = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
insertion_sort_visual(numbers)