import matplotlib.pyplot as plt

# Отсортированный массив
numbers = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
target = 36
n = len(numbers)

# Настройка графика
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title(f"Визуализация: Бинарный поиск числа {target}", fontsize=14)
ax.axis('off')

# Создаем столбцы и текстовые подписи
bars = ax.bar(range(n), numbers, color='lightblue')
texts = [ax.text(i, numbers[i] + 1.5, str(numbers[i]), ha='center', va='bottom', fontsize=11) for i in range(n)]

# Функция для обновления кадра
def draw_frame(delay=0.8):
    plt.draw()
    plt.pause(delay)

left = 0
right = n - 1

print(f"Ищем число {target}...")
draw_frame(1.0) # Пауза перед началом

while left <= right:
    mid = (left + right) // 2
    
    # 1. Сначала возвращаем всем элементам в диапазоне [left, right] голубой цвет
    for i in range(left, right + 1):
        bars[i].set_color('lightblue')
        
    # 2. Подсвечиваем серединный элемент зеленым
    bars[mid].set_color('green')
    print(f"Проверяем середину: индекс {mid}, значение {numbers[mid]}")
    draw_frame(1.0)

    if numbers[mid] == target:
        # НАЙДЕНО!
        bars[mid].set_color('#FFA500') # Красим в оранжевый
        print(f"Элемент {target} найден по индексу {mid}!")
        draw_frame(1.5)
        break
        
    elif numbers[mid] > target:
        # Искомое число меньше, отбрасываем правую половину
        print(f"{numbers[mid]} > {target}. Отбрасываем правую часть.")
        for i in range(mid, right + 1):
            bars[i].set_color('gray') # Красим отброшенные в серый
        right = mid - 1
        draw_frame(0.8)
        
    else:
        # Искомое число больше, отбрасываем левую половину
        print(f"{numbers[mid]} < {target}. Отбрасываем левую часть.")
        for i in range(left, mid + 1):
            bars[i].set_color('gray') # Красим отброшенные в серый
        left = mid + 1
        draw_frame(0.8)

# Если не нашли (цикл прервался по условию left > right)
if left > right:
    print("Элемент не найден!")
    ax.set_title(f"Элемент {target} не найден (границы пересеклись)", fontsize=14)

plt.show()