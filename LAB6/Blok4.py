# Ввод размера массива
N = int(input("Введите количество элементов в массиве: "))

# Ввод элементов массива
array = []
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)

# Нахождение минимального элемента и его индекса
min_value = array[0]
min_index = 0

for index in range(1, N):
    if array[index] < min_value:
        min_value = array[index]
        min_index = index

print(f"Минимальный элемент: {min_value}")
print(f"Индекс минимального элемента: {min_index}")


# Ввод размера массива
N = int(input("Введите количество элементов в массиве: "))

# Ввод элементов массива
array = []
for i in range(N):
    element = int(input(f"Введите элемент {i + 1}: "))
    array.append(element)

# Создание новых массивов для положительных и отрицательных элементов
positive_array = []
negative_or_zero_array = []

for element in array:
    if element > 0:
        positive_array.append(element)
    else:
        negative_or_zero_array.append(element)

print("Положительные элементы:", positive_array)
print("Неположительные элементы:", negative_or_zero_array)
