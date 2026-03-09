# -*- coding: utf-8 -*-
"""
БЫСТРЫЙ СТАРТ - Примеры задач ЕГЭ по информатике
"""

print("=" * 60)
print("ЗАДАЧА 5: Системы счисления")
print("=" * 60)

print("\nУСЛОВИЕ:")
print("Сколько существует натуральных чисел x, для которых:")
print("10110(2) <= x <= 101(8)")
print("(где (2) - двоичная система, (8) - восьмеричная)")

# Решение
left = int('10110', 2)   # Двоичное число в десятичное
right = int('101', 8)     # Восьмеричное число в десятичное

print(f"\n10110(2) = {left}")
print(f"101(8) = {right}")

# Количество натуральных чисел в диапазоне [left, right]
count = right - left + 1
print(f"\nКоличество чисел: {count}")

print("\n" + "=" * 60)
print("ЗАДАЧА 16: Рекурсия")
print("=" * 60)

print("\nУСЛОВИЕ:")
print("def F(n):")
print("    if n > 2:")
print("        return F(n - 1) + F(n - 2)")
print("    else:")
print("        return n")
print("\nЧему равно F(8)?")

# Решение
def F(n):
    if n > 2:
        return F(n - 1) + F(n - 2)
    else:
        return n

print("\nПошаговое вычисление:")
for i in range(1, 9):
    print(f"F({i}) = {F(i)}")

print(f"\nОТВЕТ: F(8) = {F(8)}")

print("\n" + "=" * 60)
print("ЗАДАЧА 17: Последовательности")
print("=" * 60)

print("\nУСЛОВИЕ:")
print("В последовательности найти пары элементов, где:")
print("1. Хотя бы одно число кратно 43")
print("2. Сумма пары меньше максимального элемента, кратного 43")

# Пример данных
numbers = [43, 86, 100, 129, 150, 200, 215, 430, 500, 645]

# Находим максимальный элемент, кратный 43
max_43 = max([x for x in numbers if x % 43 == 0])
print(f"\nЧисла: {numbers}")
print(f"Макс. элемент, кратный 43: {max_43}")

# Ищем пары
count = 0
max_sum = 0

for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] % 43 == 0 or numbers[j] % 43 == 0):
            pair_sum = numbers[i] + numbers[j]
            if pair_sum < max_43:
                count += 1
                max_sum = max(max_sum, pair_sum)

print(f"\nНайдено пар: {count}")
print(f"Максимальная сумма: {max_sum}")

print("\n" + "=" * 60)
print("ЗАДАЧА 25: Делители чисел")
print("=" * 60)

print("\nУСЛОВИЕ:")
print("Найти числа от 100 до 200 с ровно 5 делителями")

def count_divisors(n):
    """Подсчитывает количество делителей числа n"""
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

# Решение
found = []
for num in range(100, 201):
    if count_divisors(num) == 5:
        found.append(num)

print(f"\nНайдено чисел: {len(found)}")
print(f"Числа: {found}")

# Проверка
print("\nПроверка (должны быть 4-е степени простых чисел):")
for num in found:
    fourth_root = round(num ** 0.25)
    if fourth_root ** 4 == num:
        print(f"{num} = {fourth_root}^4")

print("\n" + "=" * 60)
print("ОТЛИЧНО! Все примеры работают!")
print("=" * 60)
print("\nТеперь открой папку 'ege_tasks' и изучай задачи подробнее!")
print("Начни с task_05_systems, потом task_16_recursion и т.д.")
print("\nТакже смотри:")
print("- ege_tasks/CHEATSHEET.md - шпаргалка по Python")
print("- ege_tasks/practice/exercises.py - упражнения для тренировки")
