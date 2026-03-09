# -*- coding: utf-8 -*-
"""
ЗАДАЧА 27 - Сложная оптимизация (файл А - простой перебор)

УСЛОВИЕ:
Дана последовательность из N натуральных чисел.
Рассматриваются все пары элементов с индексами i и j (i < j),
таких что разность j - i делится на 3.

Найдите максимальную сумму такой пары.

Файл А (малый): N = 7
"""

# Создаём тестовый файл A
test_data_a = [10, 3, 6, 12, 9, 15, 5]

with open('task27_A.txt', 'w') as f:
    f.write(f"{len(test_data_a)}\n")
    for num in test_data_a:
        f.write(f"{num}\n")

print("=" * 60)
print("ЗАДАЧА 27 - Файл А (простой перебор)")
print("=" * 60)

# Читаем файл
with open('task27_A.txt', 'r') as f:
    n = int(f.readline())
    numbers = [int(f.readline().strip()) for _ in range(n)]

print(f"\nДанные: {numbers}")
print(f"N = {n}\n")

# Решение для файла А: прямой перебор
max_sum = float('-inf')
best_pair = None

print("Проверяем пары:")
for i in range(n):
    for j in range(i + 1, n):
        if (j - i) % 3 == 0:
            pair_sum = numbers[i] + numbers[j]
            print(f"  i={i}, j={j}: {numbers[i]} + {numbers[j]} = {pair_sum}")

            if pair_sum > max_sum:
                max_sum = pair_sum
                best_pair = (i, j)

print("\n" + "=" * 60)
print(f"ОТВЕТ: Максимальная сумма = {max_sum}")
print(f"Пара: индексы {best_pair}, значения {numbers[best_pair[0]]} + {numbers[best_pair[1]]}")
print("=" * 60)

print("\n" + "=" * 60)
print("ВАЖНО для файла Б (большой):")
print("=" * 60)
print("""
Для большого файла (N ~ 100000) перебор не подойдёт!

Оптимизация:
1. Группируем элементы по остатку индекса от деления на 3
2. Для каждого остатка храним максимальные элементы
3. Проверяем только осмысленные комбинации

Пример оптимизированного решения:
  - Создаём 3 списка: для индексов i % 3 == 0, 1, 2
  - Для пары (i, j) где (j-i) % 3 == 0, остатки i и j одинаковы
  - Берём два максимальных элемента из каждой группы
""")
