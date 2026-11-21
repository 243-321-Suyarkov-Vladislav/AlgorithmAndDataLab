import matplotlib.pyplot as plt
import time

# Массив с картинки
numbers = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
n = len(numbers)

# Настройка графика
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title("Сортировка пузырьком (Визуализация)", fontsize=14)
ax.axis('off') # Убираем оси

# Создаем столбцы и текстовые подписи
bars = ax.bar(range(n), numbers, color='lightblue')
texts = [ax.text(i, numbers[i] + 1.5, str(numbers[i]), ha='center', va='bottom', fontsize=11) for i in range(n)]

# Функция для перерисовки графика
def draw_frame(delay=0.3):
    plt.draw()
    plt.pause(delay) # Пауза, которая и создает эффект анимации

print("Начальный массив:", numbers)

# Основной алгоритм сортировки с анимацией
for i in range(n):
    swapped = False
    print(f"\n--- Проход {i + 1} ---")
    
    for j in range(0, n - i - 1):
        # 1. Подсвечиваем текущую пару зеленым
        bars[j].set_color('green')
        bars[j+1].set_color('green')
        draw_frame(0.2) # Короткая пауза, чтобы увидеть зеленые столбцы
        
        # 2. Если нужно поменять местами
        if numbers[j] > numbers[j + 1]:
            # Меняем в массиве
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
            
            # Меняем высоту и текст столбцов на графике
            bars[j].set_height(numbers[j])
            bars[j+1].set_height(numbers[j+1])
            texts[j].set_y(numbers[j] + 1.5)
            texts[j+1].set_y(numbers[j+1] + 1.5)
            texts[j].set_text(str(numbers[j]))
            texts[j+1].set_text(str(numbers[j+1]))
            
            print(f"Меняем {numbers[j+1]} и {numbers[j]}: {numbers}")
            draw_frame(0.3) # Пауза, чтобы увидеть сам обмен
            
        # 3. Возвращаем голубой цвет (если это не последний отсортированный элемент)
        if j >= n - i - 1:
            bars[j].set_color('#FFA500')
        else:
            bars[j].set_color('lightblue')
        bars[j+1].set_color('lightblue')
            
    # После прохода крайний правый элемент встает на свое место (красим в оранжевый)
    bars[n - i - 1].set_color('#FFA500') # Оранжевый цвет
    draw_frame(0.3)
    
    if not swapped:
        print("Обменов не было. Массив отсортирован досрочно.")
        # Красим всё оставшееся в оранжевый
        for k in range(n - i - 1):
            bars[k].set_color('#FFA500')
        draw_frame(0.5)
        break

print("\nОтсортированный массив:", numbers)
plt.show() # Оставляем окно открытым в конце