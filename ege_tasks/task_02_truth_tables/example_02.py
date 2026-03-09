# -*- coding: utf-8 -*-
"""
ЗАДАЧА 2 - Таблицы истинности (сложнее)

УСЛОВИЕ:
Сколько существует различных наборов значений логических переменных
x1, x2, ..., x6, которые удовлетворяют всем перечисленным ниже условиям?

(x1 -> x2) and (x3 -> x4) and (x5 -> x6) == 1
(x1 and x3 and x5) -> (x2 or x4 or x6) == 1

В ответе не учитываются наборы переменных, где все переменные равны 0.
"""

from itertools import product

# Определяем импликацию: A -> B это (не A) или B
def implies(a, b):
    return (not a) or b

count = 0
valid_sets = []

for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    # Пропускаем набор, где все нули
    if x1 == 0 and x2 == 0 and x3 == 0 and x4 == 0 and x5 == 0 and x6 == 0:
        continue

    # Проверяем первое условие
    cond1 = implies(x1, x2) and implies(x3, x4) and implies(x5, x6)

    # Проверяем второе условие
    cond2 = implies(x1 and x3 and x5, x2 or x4 or x6)

    if cond1 and cond2:
        count += 1
        valid_sets.append((x1, x2, x3, x4, x5, x6))

print(f"Найдено наборов: {count}")
print(f"\nПервые 5 наборов:")
for i, s in enumerate(valid_sets[:5], 1):
    print(f"{i}. x1={s[0]}, x2={s[1]}, x3={s[2]}, x4={s[3]}, x5={s[4]}, x6={s[5]}")

print("\n" + "=" * 60)
print("ВАЖНО: Импликация A -> B это то же самое, что (не A) или B")
print("Таблица истинности импликации:")
print("A | B | A->B")
print("0 | 0 |  1")
print("0 | 1 |  1")
print("1 | 0 |  0")
print("1 | 1 |  1")
print("=" * 60)
