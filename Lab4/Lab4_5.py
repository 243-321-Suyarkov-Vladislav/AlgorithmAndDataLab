def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:                 # базовый случай: элемент не найден
        return -1

    mid = (left + right) // 2        # середина текущего диапазона

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13]
target = int(input("Введите искомый элемент: "))
print("Индекс:", binary_search(arr, target))