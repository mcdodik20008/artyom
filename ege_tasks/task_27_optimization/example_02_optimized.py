# -*- coding: utf-8 -*-
"""
ЗАДАЧА 27 - Сложная оптимизация (файл Б - оптимизированное решение)

Оптимизированный алгоритм для больших данных (N ~ 100000)
"""

import random

# Создаём большой тестовый файл Б
random.seed(42)
N_big = 10000
test_data_b = [random.randint(1, 10000) for _ in range(N_big)]

with open('task27_B.txt', 'w') as f:
    f.write(f"{N_big}\n")
    for num in test_data_b:
        f.write(f"{num}\n")

print("=" * 60)
print("ЗАДАЧА 27 - Файл Б (оптимизированное решение)")
print("=" * 60)

# Читаем файл
with open('task27_B.txt', 'r') as f:
    n = int(f.readline())
    numbers = [int(f.readline().strip()) for _ in range(n)]

print(f"\nN = {n} (большой файл!)")
print(f"Первые 10 чисел: {numbers[:10]}")

# ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ
# Группируем элементы по остатку индекса при делении на 3

groups = {0: [], 1: [], 2: []}

for i, num in enumerate(numbers):
    remainder = i % 3
    groups[remainder].append(num)

print(f"\nРазбиение по группам:")
for r in range(3):
    print(f"  Остаток {r}: {len(groups[r])} элементов")

# Для каждой группы находим два максимальных элемента
# (чтобы получить максимальную сумму пары)

max_sum = float('-inf')

for remainder in range(3):
    group = groups[remainder]

    if len(group) >= 2:
        # Сортируем группу и берём два максимальных
        sorted_group = sorted(group, reverse=True)
        pair_sum = sorted_group[0] + sorted_group[1]

        print(f"\nГруппа {remainder}: топ-2 = {sorted_group[0]}, {sorted_group[1]}")
        print(f"  Сумма: {pair_sum}")

        if pair_sum > max_sum:
            max_sum = pair_sum

print("\n" + "=" * 60)
print(f"ОТВЕТ: Максимальная сумма = {max_sum}")
print("=" * 60)

# Сравнение времени работы
print("\n" + "=" * 60)
print("СРАВНЕНИЕ АЛГОРИТМОВ:")
print("=" * 60)

import time

# Наивный алгоритм (только для малых данных)
def naive_solution(nums):
    max_s = float('-inf')
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (j - i) % 3 == 0:
                max_s = max(max_s, nums[i] + nums[j])
    return max_s

# Оптимизированный алгоритм
def optimized_solution(nums):
    groups = {0: [], 1: [], 2: []}
    for i, num in enumerate(nums):
        groups[i % 3].append(num)

    max_s = float('-inf')
    for r in range(3):
        if len(groups[r]) >= 2:
            sorted_g = sorted(groups[r], reverse=True)
            max_s = max(max_s, sorted_g[0] + sorted_g[1])
    return max_s

# Тестируем на малых данных
small_data = [10, 3, 6, 12, 9, 15, 5]

start = time.time()
result_naive = naive_solution(small_data)
time_naive = time.time() - start

start = time.time()
result_opt = optimized_solution(small_data)
time_opt = time.time() - start

print(f"\nМалые данные (N=7):")
print(f"  Наивный: {result_naive} (время: {time_naive*1000:.4f} мс)")
print(f"  Оптимизированный: {result_opt} (время: {time_opt*1000:.4f} мс)")

# Для больших данных только оптимизированный
start = time.time()
result_big = optimized_solution(numbers)
time_big = time.time() - start

print(f"\nБольшие данные (N={N_big}):")
print(f"  Оптимизированный: {result_big} (время: {time_big*1000:.2f} мс)")
print(f"\nНаивный алгоритм занял бы примерно {time_big * (N_big**2 / 49):.0f} секунд!")
