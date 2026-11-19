class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None: return Node(value)
    if value < root.value: root.left = insert(root.left, value)
    else: root.right = insert(root.right, value)
    return root

def inorder_traversal_visual(root, depth=0):
    if root:
        # Сначала идем влево (сдвигаем отступ)
        print("  " * depth + f"-> Идем влево от {root.value}")
        inorder_traversal_visual(root.left, depth + 1)
        
        # Печатаем корень
        print("  " * depth + f"ВЫВОД: {root.value}")
        
        # Затем идем вправо
        print("  " * depth + f"-> Идем вправо от {root.value}")
        inorder_traversal_visual(root.right, depth + 1)

tree = None
for val in [50, 30, 20, 40, 70, 60, 80]:
    tree = insert(tree, val)

print("Трассировка симметричного обхода (In-order):")
inorder_traversal_visual(tree)