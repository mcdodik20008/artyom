"""
ЗАДАЧА 25 - Делители чисел

Условие:
Найдите все натуральные числа в диапазоне [150000, 160000],
у которых ровно 5 делителей.
Выведите их в порядке возрастания.
"""

def count_divisors(n):
    """Подсчитывает количество делителей числа n"""
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:  # Если i не является квадратным корнем
                count += 1
        i += 1
    return count

# Решение
numbers_with_5_divisors = []

for num in range(150000, 160001):
    if count_divisors(num) == 5:
        numbers_with_5_divisors.append(num)

print(f"Найдено чисел с 5 делителями: {len(numbers_with_5_divisors)}")
print("\nЧисла:")
for num in numbers_with_5_divisors:
    print(num)

# Важное свойство: 5 делителей имеют только числа вида p^4,
# где p - простое число
# Проверим:
print("\nПроверка (должны быть четвёртые степени простых чисел):")
for num in numbers_with_5_divisors:
    # Проверяем, является ли число четвёртой степенью
    fourth_root = round(num ** 0.25)
    if fourth_root ** 4 == num:
        print(f"{num} = {fourth_root}^4")
