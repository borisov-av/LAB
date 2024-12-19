districts = [
    (150, 50),  # Район 1
    (200, 80),  # Район 2
    (300, 100), # Район 3
    (400, 150), # Район 4
    (250, 60),  # Район 5
    (180, 45),  # Район 6
    (220, 70),  # Район 7
    (350, 120), # Район 8
    (400, 200), # Район 9
    (500, 250), # Район 10
    (600, 300), # Район 11
    (700, 350)  # Район 12
]

total_population = 0
total_area = 0

for population, area in districts:
    total_population += population
    total_area += area

average_density = total_population / total_area
print(f"Средняя плотность населения по области: {average_density:.2f} тыс. чел./км²")

gift = 1  # Начальный подарок в долларах
age = 1   # Начальный возраст
target_amount = 100  # Целевая сумма

while gift <= target_amount:
    age += 1  # Увеличиваем возраст
    gift = gift * 2 + age  # Рассчитываем новый подарок

print(f"К дню рождения {age} подарок превысит {target_amount} долларов.")
