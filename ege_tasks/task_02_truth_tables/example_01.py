# -*- coding: utf-8 -*-
"""
ЗАДАЧА 2 - Таблицы истинности

УСЛОВИЕ:
Логическая функция F задаётся выражением:
(x <= y) or (z <= w)

Определите, сколько существует различных наборов значений переменных x, y, z, w,
при которых функция F истинна.
"""

from itertools import product

# Решение 1: Прямой перебор
count = 0

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                # Вычисляем функцию
                result = (x <= y) or (z <= w)
                if result:
                    count += 1
                    print(f"x={x}, y={y}, z={z}, w={w} -> {result}")

print(f"\nСпособ 1: Найдено наборов = {count}")

# Решение 2: С использованием itertools.product (РЕКОМЕНДУЕТСЯ для ЕГЭ!)
count2 = 0

for x, y, z, w in product([0, 1], repeat=4):
    if (x <= y) or (z <= w):
        count2 += 1

print(f"Способ 2: Найдено наборов = {count2}")

# Решение 3: Компактный вариант
count3 = sum(1 for x, y, z, w in product([0, 1], repeat=4) if (x <= y) or (z <= w))
print(f"Способ 3 (одна строка): {count3}")

print("\n" + "=" * 60)
print("СОВЕТ: Для ЕГЭ используй itertools.product - это быстро и надёжно!")
print("=" * 60)
