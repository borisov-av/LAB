def is_armstrong(number):
    # Преобразуем число в строку для удобства работы с цифрами
    digits = [int(d) for d in str(number)]
    n = len(digits)
    # Вычисляем сумму цифр, возведенных в степень n
    return sum(d ** n for d in digits) == number

def find_armstrong_numbers(k):
    armstrong_numbers = []
    for num in range(1, k + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

def geometric_progression(a, r, n):
    # Базовый случай: первый член (n = 1)
    if n == 1:
        return a
    else:
        # Рекурсивный случай: a * r^(n-1)
        return r * geometric_progression(a, r, n - 1)

# Пример использования
first_term = 2  # Первый член прогрессии
common_ratio = 3  # Знаменатель (общий множитель)
n = 5  # Позиция члена, который мы хотим получить
nth_term = geometric_progression(first_term, common_ratio, n)
print(f"{n}-й член геометрической прогрессии: {nth_term}")
