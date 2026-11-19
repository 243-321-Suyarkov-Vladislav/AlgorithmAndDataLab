def hanoi(n, source, target, auxiliary):
    if n == 0:              # базовый случай: переносить нечего
        return
    hanoi(n - 1, source, auxiliary, target)  # переносим n-1 дисков на вспомогательный стержень
    print(f"Переместить диск {n}: {source} -> {target}")
    hanoi(n - 1, auxiliary, target, source)  # переносим n-1 дисков на целевой стержень

n = int(input("Введите количество дисков: "))
hanoi(n, "A", "C", "B")