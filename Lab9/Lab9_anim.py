import matplotlib.pyplot as plt

# Массив с картинки
numbers = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(numbers)

# Настройка графика
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title("Визуализация: Сортировка выбором", fontsize=14)
ax.axis('off')

# Создаем столбцы и текстовые подписи
bars = ax.bar(range(n), numbers, color='lightblue')
texts = [ax.text(i, numbers[i] + 1.5, str(numbers[i]), ha='center', va='bottom', fontsize=11) for i in range(n)]

def draw_frame(delay=0.4):
    plt.draw()
    plt.pause(delay)

print("Начальный массив:", numbers)

# Основной алгоритм
for i in range(n - 1):
    min_idx = i
    bars[min_idx].set_color('green') # Подсвечиваем текущий минимум зеленым
    draw_frame(0.3)
    
    for j in range(i + 1, n):
        # Подсвечиваем элемент, который сейчас проверяем
        bars[j].set_color('red')
        draw_frame(0.15)
        
        if numbers[j] < numbers[min_idx]:
            # Если нашли новый минимум, старый возвращаем в голубой
            bars[min_idx].set_color('lightblue')
            min_idx = j
            bars[min_idx].set_color('green')
            draw_frame(0.3)
        else:
            # Если это не минимум, возвращаем ему голубой цвет
            bars[j].set_color('lightblue')
            
    # Когда внутренний цикл завершен, делаем обмен (если нужно)
    if min_idx != i:
        # Меняем значения в массиве
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        
        # Обновляем визуализацию (высоту и текст)
        bars[i].set_height(numbers[i])
        texts[i].set_y(numbers[i] + 1.5)
        texts[i].set_text(str(numbers[i]))
        
        bars[min_idx].set_height(numbers[min_idx])
        texts[min_idx].set_y(numbers[min_idx] + 1.5)
        texts[min_idx].set_text(str(numbers[min_idx]))
        
        print(f"Шаг {i+1}: Меняем {numbers[min_idx]} и {numbers[i]}: {numbers}")
        draw_frame(0.5)
    
    # Элемент i встал на свое место, красим его в оранжевый (отсортирован)
    bars[i].set_color('#FFA500')
    if min_idx == i:
        bars[min_idx].set_color('#FFA500')
    draw_frame(0.3)

# Последний элемент автоматически оказывается на своем месте
bars[n-1].set_color('#FFA500')
draw_frame(0.5)

print("\nОтсортированный массив:", numbers)
plt.show()