def selection_sort_visual(arr):
    n = len(arr)
    print("Начальный массив:", arr)
    
    for i in range(n - 1):
        min_idx = i
        print(f"\n--- Шаг {i + 1}: Ищем минимум для позиции {i} (текущий элемент {arr[i]}) ---")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"  Нашли новый минимум: {arr[j]} (индекс {j})")
                
        if min_idx != i:
            print(f"  Меняем местами {arr[i]} и {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  Текущий массив: {arr}")
        else:
            print(f"  Элемент {arr[i]} уже на своем месте.")
            
    return arr

numbers = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
selection_sort_visual(numbers)