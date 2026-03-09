# -*- coding: utf-8 -*-
"""
ЗАДАЧА 26 - Жадные алгоритмы и сортировка

УСЛОВИЕ:
В магазин привезли N товаров. Каждый товар характеризуется весом.
На складе есть K стеллажей, каждый стеллаж выдерживает не более W кг.
Нужно разместить максимальное количество товаров на стеллажи.

ВОПРОС 1: Какое максимальное количество товаров можно разместить?
ВОПРОС 2: Какой максимальный вес товара, который остался неразмещённым?
"""

# Генерируем тестовые данные
import random
random.seed(42)

N = 50  # Количество товаров
K = 5   # Количество стеллажей
W = 100 # Максимальный вес на стеллаж

# Веса товаров (от 10 до 60 кг)
weights = [random.randint(10, 60) for _ in range(N)]

# Сохраняем в файл
with open('task26_input.txt', 'w') as f:
    f.write(f"{N} {K} {W}\n")
    for w in weights:
        f.write(f"{w}\n")

print("=" * 60)
print("ЗАДАЧА 26: Размещение товаров на стеллажи")
print("=" * 60)

# Читаем из файла
with open('task26_input.txt', 'r') as f:
    n, k, max_weight = map(int, f.readline().split())
    weights = [int(f.readline().strip()) for _ in range(n)]

print(f"\nИсходные данные:")
print(f"  Товаров: {n}")
print(f"  Стеллажей: {k}")
print(f"  Макс. вес на стеллаж: {max_weight} кг")
print(f"  Веса товаров (первые 10): {weights[:10]}")

# ЖАДНЫЙ АЛГОРИТМ: сортируем товары по возрастанию веса
# и размещаем на наименее загруженный стеллаж

weights_sorted = sorted(weights)  # Сортируем по возрастанию
shelves = [0] * k  # Текущая загрузка каждого стеллажа
placed = []  # Размещённые товары
not_placed = []  # Неразмещённые товары

for weight in weights_sorted:
    # Ищем стеллаж с минимальной загрузкой, который может вместить товар
    best_shelf = -1
    min_load = float('inf')

    for i in range(k):
        if shelves[i] + weight <= max_weight:
            if shelves[i] < min_load:
                min_load = shelves[i]
                best_shelf = i

    if best_shelf != -1:
        # Размещаем товар
        shelves[best_shelf] += weight
        placed.append(weight)
    else:
        # Не можем разместить
        not_placed.append(weight)

print("\n" + "=" * 60)
print("РЕЗУЛЬТАТ:")
print("=" * 60)

print(f"\nРазмещено товаров: {len(placed)}")
print(f"Не размещено товаров: {len(not_placed)}")

print("\nЗагрузка стеллажей:")
for i, load in enumerate(shelves, 1):
    percentage = (load / max_weight) * 100
    print(f"  Стеллаж {i}: {load}/{max_weight} кг ({percentage:.1f}%)")

if not_placed:
    max_not_placed = max(not_placed)
    print(f"\nМаксимальный вес неразмещённого товара: {max_not_placed} кг")
else:
    print("\nВсе товары размещены!")

print("\n" + "=" * 60)
print("ОТВЕТЫ:")
print("=" * 60)
print(f"1. Количество размещённых товаров: {len(placed)}")
print(f"2. Макс. вес неразмещённого товара: {max(not_placed) if not_placed else 0}")
