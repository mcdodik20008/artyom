# -*- coding: utf-8 -*-
"""
ЗАДАЧИ 19, 20, 21 - Теория игр (Куча камней)

УСЛОВИЕ:
Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит куча камней. Игроки ходят по очереди, первый ходит Петя.
За один ход игрок может:
  - добавить 1 камень
  - добавить 2 камня
  - умножить количество камней на 2

Игра завершается, когда в куче становится >= 29 камней.
Победителем считается игрок, сделавший последний ход.

ЗАДАЧА 19: При каком наименьшем S, Петя выигрывает СВОИМ ПЕРВЫМ ходом?
ЗАДАЧА 20: При каких S, Ваня выигрывает своим ПЕРВЫМ ходом?
           (как бы Петя ни играл, Ваня побеждает первым ходом)
ЗАДАЧА 21: При каких S, Петя выигрывает СВОИМ ВТОРЫМ ходом?
           (при правильной игре обоих игроков)
"""

from functools import lru_cache

# Финишная позиция
FINISH = 29

@lru_cache(maxsize=None)
def can_win(stones, is_petya_turn):
    """
    Возвращает True, если текущий игрок может выиграть из данной позиции.
    is_petya_turn = True, если сейчас ход Пети
    """
    # Базовый случай: если >= FINISH, игра закончена
    if stones >= FINISH:
        return False  # Текущий игрок уже не может ходить (игра закончена)

    # Возможные ходы
    moves = [stones + 1, stones + 2, stones * 2]

    for new_stones in moves:
        if new_stones >= FINISH:
            # Можем закончить игру этим ходом - выигрываем!
            return True

        # Рекурсивно проверяем, может ли противник выиграть
        if not can_win(new_stones, not is_petya_turn):
            # Если противник не может выиграть после нашего хода, мы выигрываем!
            return True

    # Если ни один ход не ведёт к победе, текущий игрок проигрывает
    return False

print("=" * 60)
print("ТЕОРИЯ ИГР: Анализ всех позиций")
print("=" * 60)

# ЗАДАЧА 19: Петя выигрывает первым ходом
print("\nЗАДАЧА 19: При каких S Петя выигрывает ПЕРВЫМ ходом?")
print("-" * 60)

task19_answers = []
for s in range(1, FINISH):
    moves = [s + 1, s + 2, s * 2]
    # Проверяем, есть ли ход, который сразу приводит к выигрышу
    for move in moves:
        if move >= FINISH:
            task19_answers.append(s)
            break

print(f"Ответы: {task19_answers}")
print(f"Наименьшее S: {min(task19_answers) if task19_answers else 'нет'}")

# ЗАДАЧА 20: Ваня выигрывает первым ходом
print("\nЗАДАЧА 20: При каких S Ваня выигрывает ПЕРВЫМ ходом?")
print("(после любого хода Пети, Ваня может выиграть следующим ходом)")
print("-" * 60)

task20_answers = []
for s in range(1, FINISH):
    # Петя не может выиграть сразу
    petya_wins_immediately = False
    moves_petya = [s + 1, s + 2, s * 2]

    for move in moves_petya:
        if move >= FINISH:
            petya_wins_immediately = True
            break

    if petya_wins_immediately:
        continue

    # Проверяем, что после ЛЮБОГО хода Пети, Ваня может выиграть
    vanya_can_always_win = True

    for move_petya in moves_petya:
        if move_petya >= FINISH:
            continue

        # Проверяем, может ли Ваня выиграть после этого хода Пети
        moves_vanya = [move_petya + 1, move_petya + 2, move_petya * 2]

        vanya_wins = False
        for move_vanya in moves_vanya:
            if move_vanya >= FINISH:
                vanya_wins = True
                break

        if not vanya_wins:
            vanya_can_always_win = False
            break

    if vanya_can_always_win:
        task20_answers.append(s)

print(f"Ответы: {task20_answers}")

# ЗАДАЧА 21: Петя выигрывает вторым ходом
print("\nЗАДАЧА 21: При каких S Петя выигрывает ВТОРЫМ ходом?")
print("(при правильной игре обоих)")
print("-" * 60)

task21_answers = []
for s in range(1, FINISH):
    # Петя не должен выигрывать первым ходом
    if s in task19_answers:
        continue

    # Ваня не должен выигрывать первым ходом
    if s in task20_answers:
        continue

    # Проверяем, что Петя может выиграть вторым ходом
    # Это значит, что у Пети есть ход, после которого он попадает в позицию из задачи 20
    petya_can_win = False

    moves_petya = [s + 1, s + 2, s * 2]
    for move_petya in moves_petya:
        if move_petya >= FINISH:
            continue

        # Если после хода Пети получается позиция из задачи 20, то Петя выигрывает
        if move_petya in task20_answers:
            petya_can_win = True
            break

    if petya_can_win:
        task21_answers.append(s)

print(f"Ответы: {task21_answers}")

print("\n" + "=" * 60)
print("ИТОГОВЫЕ ОТВЕТЫ:")
print("=" * 60)
print(f"Задача 19 (Петя, 1-й ход):  {min(task19_answers) if task19_answers else 'нет'}")
print(f"Задача 20 (Ваня, 1-й ход):  {task20_answers}")
print(f"Задача 21 (Петя, 2-й ход):  {task21_answers}")
