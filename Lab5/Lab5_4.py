N = int(input("Введите N: "))
a = list(map(int, input("Введите элементы массива через пробел: ").split()))

left = 0
right = N - 1
result = []

while left <= right:
    result.append(a[left])
    if left != right:
        result.append(a[right])
    left += 1
    right -= 1

print(result)