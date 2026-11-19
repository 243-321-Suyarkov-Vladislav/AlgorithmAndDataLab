import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import deque

# Настройка графика
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 3)
ax.axis('off')
ax.set_title("Визуализация: Работа очереди (FIFO)", fontsize=14)

q = deque()

def draw_queue(action_text=""):
    ax.clear() # Очищаем предыдущий кадр
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 3)
    ax.axis('off')
    ax.set_title(action_text, fontsize=14)
    
    # Рисуем элементы
    for i, item in enumerate(q):
        # Рисуем прямоугольник
        rect = patches.Rectangle((i + 0.5, 0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        # Пишем текст внутри
        ax.text(i + 1, 1, str(item), ha='center', va='center', fontsize=14, fontweight='bold')
        
    # Подписи "Начало" и "Конец"
    if len(q) > 0:
        ax.text(-0.2, 1, "Выход\n<--", ha='right', va='center', color='red', fontweight='bold')
        ax.text(len(q) + 1.2, 1, "--> Вход\n(Конец)", ha='left', va='center', color='green', fontweight='bold')
        
    plt.draw()
    plt.pause(1.0) # Пауза 1 секунда

# 1. Добавляем элементы
for i in range(1, 5):
    q.append(i * 10)
    draw_queue(f"Добавляем {i*10} в конец очереди (Enqueue)")
    
plt.pause(0.5)

# 2. Извлекаем элементы
while len(q) > 0:
    first = q[0]
    # Подсвечиваем первый элемент красным перед удалением
    ax.clear()
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 3); ax.axis('off')
    ax.set_title(f"Извлекаем {first} из начала очереди (Dequeue)", fontsize=14)
    
    for i, item in enumerate(q):
        color = '#ff9999' if i == 0 else 'lightblue' # Первый делаем красным
        rect = patches.Rectangle((i + 0.5, 0.5), 1, 1, linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(i + 1, 1, str(item), ha='center', va='center', fontsize=14, fontweight='bold')
        
    plt.draw()
    plt.pause(1.0) # Пауза, чтобы увидеть, кто уходит
    
    q.popleft() # Удаляем
    draw_queue(f"Элемент {first} извлечен")

draw_queue("Очередь пуста!")
plt.show()