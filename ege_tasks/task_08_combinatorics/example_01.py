"""
ЗАДАЧА 8 - Комбинаторика

Условие:
Сколько существует пятизначных чисел, в записи которых:
1. Используются только цифры 1, 2, 3, 4, 5
2. Число делится на 3
3. Цифры не повторяются

Решение через перебор:
"""

count = 0
numbers_found = []

# Перебираем все пятизначные числа с цифрами 1-5 без повторений
for a in range(1, 6):
    for b in range(1, 6):
        if b == a:
            continue
        for c in range(1, 6):
            if c == a or c == b:
                continue
            for d in range(1, 6):
                if d == a or d == b or d == c:
                    continue
                for e in range(1, 6):
                    if e == a or e == b or e == c or e == d:
                        continue

                    # Сформировали число
                    number = a*10000 + b*1000 + c*100 + d*10 + e

                    # Проверяем делимость на 3
                    # Число делится на 3, если сумма его цифр делится на 3
                    digit_sum = a + b + c + d + e

                    if digit_sum % 3 == 0:
                        count += 1
                        numbers_found.append(number)

print(f"Количество чисел: {count}")
print(f"\nПервые 10 найденных чисел:")
for num in numbers_found[:10]:
    print(num)

# Проверка: сумма цифр 1+2+3+4+5 = 15, делится на 3
# Поэтому ВСЕ перестановки этих цифр дадут числа, делящиеся на 3!
print(f"\nСумма цифр 1+2+3+4+5 = {1+2+3+4+5} (делится на 3)")

# Альтернативное решение через permutations
from itertools import permutations

digits = [1, 2, 3, 4, 5]
perms = list(permutations(digits))

count_alt = 0
for perm in perms:
    number = perm[0]*10000 + perm[1]*1000 + perm[2]*100 + perm[3]*10 + perm[4]
    if sum(perm) % 3 == 0:
        count_alt += 1

print(f"\nПроверка через permutations: {count_alt}")
