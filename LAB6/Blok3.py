gift = 1  # Начальный подарок в долларах
age = 1   # Начальный возраст
target_amount = 100  # Целевая сумма

while gift <= target_amount:
    age += 1  # Увеличиваем возраст
    gift = gift * 2 + age  # Рассчитываем новый подарок

print(f"К дню рождения {age} подарок превысит {target_amount} долларов.")
