class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# 1. Симметричный обход (In-order: Левое поддерево -> Корень -> Правое поддерево)
# Выводит элементы по возрастанию
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# 2. Прямой обход (Pre-order: Корень -> Левое поддерево -> Правое поддерево)
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# 3. Обратный обход (Post-order: Левое поддерево -> Правое поддерево -> Корень)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Создаем дерево
tree = None
for val in [50, 30, 20, 40, 70, 60, 80]:
    tree = insert(tree, val)

print("Симметричный обход (In-order):")
inorder_traversal(tree)
print("\nПрямой обход (Pre-order):")
preorder_traversal(tree)
print("\nОбратный обход (Post-order):")
postorder_traversal(tree)