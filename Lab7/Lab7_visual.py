def bubble_sort_visual(arr):
    n = len(arr)
    print("Начальный массив:", arr)
    
    for i in range(n):
        swapped = False # Флаг для оптимизации
        print(f"\n--- Проход {i + 1} ---")
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"Меняем {arr[j+1]} и {arr[j]}: {arr}")
        
        if not swapped:
            print("Обменов не было. Массив отсортирован досрочно.")
            break # Оптимизация: если обменов не было, массив уже отсортирован
            
    return arr

# Запуск визуализации
numbers = [5, 1, 4, 2, 8]
bubble_sort_visual(numbers)