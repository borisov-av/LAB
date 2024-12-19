def is_leap_year(year):
    """Определяет, является ли год високосным."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Високосный год
            else:
                return False  # Не високосный год
        else:
            return True  # Високосный год
    else:
        return False  # Не високосный год

def days_in_year(year):
    """Возвращает количество дней в году."""
    if is_leap_year(year):
        return 366
    else:
        return 365

# Ввод номера года
year = int(input("Введите номер года: "))
print(f"Количество дней в {year} году: {days_in_year(year)}")

