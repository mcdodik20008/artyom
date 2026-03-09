# -*- coding: utf-8 -*-
"""
ЗАДАЧА 23 - Динамическое программирование (Количество путей)

УСЛОВИЕ:
Исполнитель Калькулятор преобразует число на экране.
У исполнителя есть три команды:
  1. Прибавить 1
  2. Прибавить 2
  3. Умножить на 2

Сколько существует программ, которые число 3 преобразуют в число 20?
"""

from functools import lru_cache

# Решение 1: Рекурсия с мемоизацией
@lru_cache(maxsize=None)
def count_ways(current, target):
    """
    Подсчитывает количество способов достичь target из current
    """
    # Базовые случаи
    if current == target:
        return 1

    if current > target:
        return 0

    # Рекурсивно считаем пути для каждой команды
    ways = 0
    ways += count_ways(current + 1, target)  # Команда 1
    ways += count_ways(current + 2, target)  # Команда 2
    ways += count_ways(current * 2, target)  # Команда 3

    return ways

start = 3
finish = 20

result1 = count_ways(start, finish)
print(f"Способ 1 (рекурсия): {result1} программ")

# Решение 2: Динамическое программирование (снизу вверх)
def count_ways_dp(start, finish):
    # dp[i] = количество способов достичь числа i
    dp = [0] * (finish + 1)
    dp[start] = 1  # Один способ быть в начальной позиции

    for i in range(start, finish + 1):
        if dp[i] == 0:
            continue

        # Применяем каждую команду
        if i + 1 <= finish:
            dp[i + 1] += dp[i]

        if i + 2 <= finish:
            dp[i + 2] += dp[i]

        if i * 2 <= finish:
            dp[i * 2] += dp[i]

    return dp[finish]

result2 = count_ways_dp(start, finish)
print(f"Способ 2 (DP): {result2} программ")

# Подробный анализ
print("\n" + "=" * 60)
print("ПОДРОБНЫЙ АНАЛИЗ:")
print("=" * 60)

dp = [0] * (finish + 1)
dp[start] = 1

print(f"\nНачало: число {start}, количество путей = {dp[start]}")
print("\nПостроение таблицы путей:")

for i in range(start, finish + 1):
    if dp[i] > 0:
        print(f"\nИз позиции {i} (путей: {dp[i]}):")

        if i + 1 <= finish:
            dp[i + 1] += dp[i]
            print(f"  +1 -> {i+1} (теперь путей: {dp[i+1]})")

        if i + 2 <= finish:
            dp[i + 2] += dp[i]
            print(f"  +2 -> {i+2} (теперь путей: {dp[i+2]})")

        if i * 2 <= finish:
            dp[i * 2] += dp[i]
            print(f"  *2 -> {i*2} (теперь путей: {dp[i*2]})")

print(f"\n{'='*60}")
print(f"ОТВЕТ: {dp[finish]} программ")
print(f"{'='*60}")

# Визуализация таблицы
print("\nТаблица количества путей:")
for i in range(start, finish + 1):
    if dp[i] > 0:
        print(f"  К числу {i:2d}: {dp[i]:4d} путей")
