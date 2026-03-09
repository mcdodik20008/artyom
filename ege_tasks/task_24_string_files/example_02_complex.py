# -*- coding: utf-8 -*-
"""
ЗАДАЧА 24 - Обработка строк (сложный паттерн)

УСЛОВИЕ:
Текстовый файл содержит строку из заглавных букв латинского алфавита.
Найдите длину самой длинной подстроки, которая:
  1. Начинается с буквы C
  2. Заканчивается буквой A
  3. Содержит ровно одну букву B между ними
"""

# Создаём тестовый файл
test_string = "XYZCDDDDDBACDBACDEBACFGHCCCCCBBBBBACZZZCXBXBXBACABC"

with open('task24_input2.txt', 'w') as f:
    f.write(test_string)

print("Тестовая строка:")
print(test_string)
print(f"Длина: {len(test_string)}\n")

# Читаем файл
with open('task24_input2.txt', 'r') as f:
    text = f.read().strip()

# Решение
max_length = 0
best_substring = ""

# Ищем все подстроки от C до A
for i in range(len(text)):
    if text[i] == 'C':
        # Нашли начало, ищем конец
        for j in range(i + 1, len(text)):
            if text[j] == 'A':
                # Нашли конец, проверяем условие с B
                substring = text[i:j+1]
                count_b = substring.count('B')

                if count_b == 1:
                    length = len(substring)
                    if length > max_length:
                        max_length = length
                        best_substring = substring

print("Найденные подстроки C...B...A (с ровно одной B):")
print("-" * 60)

# Показываем все подходящие
for i in range(len(text)):
    if text[i] == 'C':
        for j in range(i + 1, len(text)):
            if text[j] == 'A':
                substring = text[i:j+1]
                if substring.count('B') == 1:
                    print(f"[{i}:{j+1}] '{substring}' (длина {len(substring)})")

print("\n" + "=" * 60)
print(f"ОТВЕТ: Максимальная длина = {max_length}")
print(f"Подстрока: '{best_substring}'")
print("=" * 60)

# Дополнительная статистика
print("\nСтатистика по файлу:")
print(f"  Букв C: {text.count('C')}")
print(f"  Букв B: {text.count('B')}")
print(f"  Букв A: {text.count('A')}")
