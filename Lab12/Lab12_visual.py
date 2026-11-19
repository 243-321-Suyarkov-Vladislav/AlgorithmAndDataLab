from collections import deque

def queue_visual():
    q = deque()
    print("Создана пустая очередь:", list(q))

    tasks = ["A", "B", "C", "D"]
    print("\n--- ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ (Enqueue) ---")
    for task in tasks:
        q.append(task)
        print(f"Добавили '{task}' -> Очередь: {list(q)}")

    print("\n--- ИЗВЛЕЧЕНИЕ ЭЛЕМЕНТОВ (Dequeue) ---")
    while len(q) > 0:
        # Смотрим, кто первый
        first = q[0]
        # Извлекаем его
        item = q.popleft()
        print(f"Извлекаем '{item}' (он был первым, т.к. {first} == {item}) -> Очередь: {list(q)}")
    
    print("\nОчередь пуста. Программа завершена.")

queue_visual()