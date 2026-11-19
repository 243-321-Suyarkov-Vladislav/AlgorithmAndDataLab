import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.x = 0
        self.y = 0

def insert(root, value):
    if root is None: return Node(value)
    if value < root.value: root.left = insert(root.left, value)
    else: root.right = insert(root.right, value)
    return root

# Функция для расчета координат узлов
def set_positions(node, x=0, y=0, x_offset=10):
    if node is None: return
    node.x = x
    node.y = y
    # Левый ребенок сдвигается влево и вниз, правый — вправо и вниз
    set_positions(node.left, x - x_offset, y - 10, x_offset / 2)
    set_positions(node.right, x + x_offset, y - 10, x_offset / 2)

# Генератор обхода (отдает узлы по одному для анимации)
def inorder_generator(node):
    if node:
        yield from inorder_generator(node.left)
        yield node
        yield from inorder_generator(node.right)

# 1. Строим дерево
tree = None
for val in [50, 30, 20, 40, 70, 60, 80]:
    tree = insert(tree, val)
set_positions(tree)

# 2. Настройка графика
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Визуализация: Симметричный обход дерева (In-order)", fontsize=14)
ax.axis('off')

# 3. Отрисовка связей (линий) и узлов (кругов)
nodes_info = []
def draw_tree(node):
    if node:
        # Рисуем линии к детям
        if node.left:
            ax.plot([node.x, node.left.x], [node.y, node.left.y], 'k-', zorder=1)
            draw_tree(node.left)
        if node.right:
            ax.plot([node.x, node.right.x], [node.y, node.right.y], 'k-', zorder=1)
            draw_tree(node.right)
        
        # Рисуем сам узел
        circle = patches.Circle((node.x, node.y), radius=3, color='lightblue', zorder=2)
        ax.add_patch(circle)
        ax.text(node.x, node.y, str(node.value), ha='center', va='center', fontsize=12, zorder=3)
        nodes_info.append((node, circle))

draw_tree(tree)
plt.xlim(-25, 25)
plt.ylim(-25, 5)
plt.draw()
plt.pause(1) # Пауза перед началом анимации

# 4. Анимация обхода
print("Порядок обхода: ", end="")
for visited_node in inorder_generator(tree):
    print(visited_node.value, end=" ")
    
    # Находим круг, который соответствует текущему узлу, и красим его в зеленый
    for node, circle in nodes_info:
        if node == visited_node:
            circle.set_color('green')
            
    plt.draw()
    plt.pause(0.8) # Задержка между шагами

print("\nОбход завершен!")
plt.show()