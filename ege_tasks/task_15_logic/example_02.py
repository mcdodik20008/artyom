# -*- coding: utf-8 -*-
"""
ЗАДАЧА 15 - Побитовые операции

УСЛОВИЕ:
На числовой прямой даны два отрезка: P = [5, 18] и Q = [12, 26].
Найдите наименьшую возможную длину такого отрезка A,
что формула

(x ∈ P) -> ((x ∈ Q) -> (x ∈ A))

тождественно истинна (то есть истинна при любом значении x).
"""

def implies(a, b):
    return (not a) or b

# Перебираем все возможные отрезки A
P = (5, 18)
Q = (12, 26)

print("Дано:")
print(f"  P = [{P[0]}, {P[1]}]")
print(f"  Q = [{Q[0]}, {Q[1]}]")

min_length = float('inf')
best_A = None

# Перебираем начало и конец отрезка A
for a_start in range(0, 30):
    for a_end in range(a_start, 30):
        A = (a_start, a_end)

        # Проверяем формулу для всех целых x в разумном диапазоне
        valid = True
        for x in range(0, 30):
            in_P = P[0] <= x <= P[1]
            in_Q = Q[0] <= x <= Q[1]
            in_A = A[0] <= x <= A[1]

            # (x ∈ P) -> ((x ∈ Q) -> (x ∈ A))
            result = implies(in_P, implies(in_Q, in_A))

            if not result:
                valid = False
                break

        if valid:
            length = a_end - a_start
            if length < min_length:
                min_length = length
                best_A = A

print(f"\nНаименьший отрезок A = [{best_A[0]}, {best_A[1]}]")
print(f"Длина отрезка: {min_length}")

# Анализ
print("\n" + "=" * 60)
print("ЛОГИЧЕСКИЙ АНАЛИЗ:")
print("=" * 60)

print("\nФормула: (x ∈ P) -> ((x ∈ Q) -> (x ∈ A))")
print("\nПреобразуем: (x ∈ P) -> ((x ∈ Q) -> (x ∈ A))")
print("             (x ∈ P) -> (не(x ∈ Q) или (x ∈ A))")
print("             не(x ∈ P) или не(x ∈ Q) или (x ∈ A)")
print("\nФормула ложна только когда:")
print("  (x ∈ P) И (x ∈ Q) И не(x ∈ A)")
print("\nТо есть x должен быть в P И в Q, но НЕ в A")

# Находим пересечение P и Q
intersection = (max(P[0], Q[0]), min(P[1], Q[1]))
print(f"\nПересечение P и Q: [{intersection[0]}, {intersection[1]}]")
print("\nЧтобы формула была истинной, A должен содержать это пересечение!")

print(f"\nМинимальный отрезок A = [{intersection[0]}, {intersection[1]}]")
print(f"Длина: {intersection[1] - intersection[0]}")

print(f"\nОТВЕТ: {intersection[1] - intersection[0]}")
