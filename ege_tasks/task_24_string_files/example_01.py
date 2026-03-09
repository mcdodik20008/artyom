# -*- coding: utf-8 -*-
"""
ЗАДАЧА 24 - Обработка текстовых файлов (поиск подстрок)

УСЛОВИЕ:
Текстовый файл содержит только заглавные буквы латинского алфавита (A-Z).
Определите максимальное количество идущих подряд символов,
среди которых нет двух одинаковых букв подряд (AA, BB, CC, ..., ZZ).
"""

# Создаём тестовый файл
test_string = "ABCDEAABCDEFFGHIJKLMNOPQRSTUVWXYZAABBBCDEFF"

with open('task24_input.txt', 'w') as f:
    f.write(test_string)

print("Тестовая строка:")
print(test_string)
print(f"Длина: {len(test_string)}\n")

# Читаем файл
with open('task24_input.txt', 'r') as f:
    text = f.read().strip()

# Решение
max_length = 0
current_length = 1  # Первый символ всегда входит

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        # Нашли повтор - сбрасываем счётчик
        max_length = max(max_length, current_length)
        current_length = 1
    else:
        current_length += 1

# Не забываем проверить последний участок
max_length = max(max_length, current_length)

print(f"Максимальная длина участка без повторов: {max_length}")

# Детальный анализ
print("\n" + "=" * 60)
print("ДЕТАЛЬНЫЙ АНАЛИЗ:")
print("=" * 60)

current_length = 1
start = 0

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        # Нашли повтор
        if current_length >= 10:  # Показываем только длинные участки
            print(f"Участок [{start}:{i}]: '{text[start:i]}' (длина {current_length})")
        start = i
        current_length = 1
    else:
        current_length += 1

# Последний участок
if current_length >= 10:
    print(f"Участок [{start}:{len(text)}]: '{text[start:]}' (длина {current_length})")

print(f"\nОТВЕТ: {max_length}")
