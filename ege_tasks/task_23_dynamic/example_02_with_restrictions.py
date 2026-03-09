# -*- coding: utf-8 -*-
"""
ЗАДАЧА 23 - Динамическое программирование (с ограничениями)

УСЛОВИЕ:
Исполнитель Калькулятор преобразует число на экране.
У исполнителя есть три команды:
  1. Прибавить 1
  2. Прибавить 2
  3. Умножить на 2

Сколько существует программ, которые число 3 преобразуют в число 25,
и при этом траектория вычислений НЕ содержит числа 11 и 18?
"""

def count_ways_with_restrictions(start, finish, forbidden):
    """
    Подсчитывает пути с учётом запрещённых чисел
    """
    # dp[i] = количество способов достичь числа i
    dp = [0] * (finish + 1)
    dp[start] = 1

    # Запрещённые числа не учитываем
    for num in forbidden:
        if num <= finish:
            dp[num] = -1  # Помечаем как запрещённое

    for i in range(start, finish + 1):
        if dp[i] == 0 or dp[i] == -1:
            continue

        # Применяем каждую команду
        commands = [
            (i + 1, "+1"),
            (i + 2, "+2"),
            (i * 2, "*2")
        ]

        for next_num, cmd in commands:
            if next_num <= finish and dp[next_num] != -1:
                if dp[next_num] == 0:
                    dp[next_num] = dp[i]
                else:
                    dp[next_num] += dp[i]

    return dp[finish] if dp[finish] != -1 else 0

start = 3
finish = 25
forbidden = [11, 18]

result = count_ways_with_restrictions(start, finish, forbidden)

print("=" * 60)
print("ЗАДАЧА С ОГРАНИЧЕНИЯМИ")
print("=" * 60)
print(f"\nНачало: {start}")
print(f"Конец: {finish}")
print(f"Запрещённые числа: {forbidden}")
print(f"\nКоличество программ: {result}")

# Сравнение с решением без ограничений
result_without = count_ways_with_restrictions(start, finish, [])
print(f"\nДля сравнения:")
print(f"  Без ограничений: {result_without} программ")
print(f"  С ограничениями: {result} программ")
print(f"  Разница: {result_without - result} программ")

# Детальный анализ
print("\n" + "=" * 60)
print("ДЕТАЛЬНАЯ ТАБЛИЦА:")
print("=" * 60)

dp = [0] * (finish + 1)
dp[start] = 1

# Помечаем запрещённые
for num in forbidden:
    if num <= finish:
        dp[num] = -1

for i in range(start, finish + 1):
    status = ""
    if dp[i] == -1:
        status = "ЗАПРЕЩЕНО"
    elif dp[i] == 0:
        status = "недостижимо"
    else:
        status = f"{dp[i]} путей"

        # Применяем команды
        if i + 1 <= finish and dp[i + 1] != -1:
            dp[i + 1] = (dp[i + 1] if dp[i + 1] > 0 else 0) + dp[i]

        if i + 2 <= finish and dp[i + 2] != -1:
            dp[i + 2] = (dp[i + 2] if dp[i + 2] > 0 else 0) + dp[i]

        if i * 2 <= finish and dp[i * 2] != -1:
            dp[i * 2] = (dp[i * 2] if dp[i * 2] > 0 else 0) + dp[i]

    print(f"  {i:2d}: {status}")

print(f"\n{'='*60}")
print(f"ОТВЕТ: {dp[finish] if dp[finish] != -1 else 0}")
print(f"{'='*60}")
