import matplotlib.pyplot as plt
import time

# Массив с ваших картинок (перемешанный)
numbers = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(numbers)

# Настройка графика
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title("Визуализация: Сортировка вставками", fontsize=14)
ax.axis('off')

# Создаем столбцы и подписи
bars = ax.bar(range(n), numbers, color='lightblue')
texts = [ax.text(i, numbers[i] + 1.5, str(numbers[i]), ha='center', va='bottom', fontsize=11) for i in range(n)]

# Функция обновления графика на экране
def draw_frame(delay=0.4):
    plt.draw()
    plt.pause(delay)

print("Начальный массив:", numbers)

# Основной алгоритм с анимацией
for i in range(1, n):
    # Первый элемент (i=0) уже считается отсортированным
    bars[0].set_color('#FFA500') 
    
    key = numbers[i]
    j = i - 1
    
    # Подсвечиваем текущий key зеленым
    bars[i].set_color('green')
    texts[i].set_text(f"{key}*") # Звездочкой помечаем, что он "в руках"
    print(f"\n--- Шаг {i}: Берем элемент {key} ---")
    draw_frame(0.5)
    
    while j >= 0 and numbers[j] > key:
        # Сдвигаем элемент вправо
        numbers[j + 1] = numbers[j]
        
        # Визуализация сдвига
        bars[j+1].set_height(numbers[j+1])
        texts[j+1].set_y(numbers[j+1] + 1.5)
        texts[j+1].set_text(str(numbers[j+1]))
        bars[j+1].set_color('red') # Красный цвет для сдвигаемого элемента
        bars[j].set_color('lightblue') # Старое место освобождается
        
        print(f"Сдвигаем {numbers[j]} вправо: {numbers}")
        draw_frame(0.3)
        
        j -= 1
        
    # Вставляем key
    numbers[j + 1] = key
    bars[j+1].set_height(numbers[j+1])
    texts[j+1].set_y(numbers[j+1] + 1.5)
    texts[j+1].set_text(str(numbers[j+1]))
    
    print(f"Вставляем {key} на позицию {j + 1}: {numbers}")
    
    # Перекрашиваем всю отсортированную часть в оранжевый
    for k in range(i + 1):
        bars[k].set_color('#FFA500')
        # Убираем звездочку у key после вставки
        texts[k].set_text(str(numbers[k]))
        
    draw_frame(0.4)

print("\nОтсортированный массив:", numbers)
plt.show()