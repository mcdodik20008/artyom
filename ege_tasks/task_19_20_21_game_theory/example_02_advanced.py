# -*- coding: utf-8 -*-
"""
ЗАДАЧИ 19, 20, 21 - Теория игр (Универсальное решение)

УНИВЕРСАЛЬНЫЙ ШАБЛОН для любой игры с кучей камней!
Просто меняй правила ходов и финиш.
"""

from functools import lru_cache

# ========== НАСТРОЙКИ ИГРЫ ==========
FINISH = 43  # Финишная позиция

def get_moves(stones):
    """Определяет возможные ходы из текущей позиции"""
    return [
        stones + 1,
        stones + 3,
        stones * 2
    ]
# ====================================

@lru_cache(maxsize=None)
def analyze_position(stones, moves_left):
    """
    Анализирует позицию и определяет, кто выигрывает.

    Возвращает:
    - 'W' если текущий игрок выигрывает
    - 'L' если текущий игрок проигрывает
    """
    # Базовый случай
    if stones >= FINISH:
        return 'L'  # Тот, кто должен ходить, проиграл (игра уже закончена)

    if moves_left == 0:
        return 'L'  # Ходы закончились

    # Получаем возможные ходы
    moves = get_moves(stones)

    # Проверяем каждый ход
    can_win = False
    can_lose = False

    for move in moves:
        if move >= FINISH:
            # Можем закончить игру - это победа!
            can_win = True
        else:
            # Смотрим, что будет после хода противника
            opponent_result = analyze_position(move, moves_left - 1)

            if opponent_result == 'L':
                # Противник проиграет - мы выигрываем!
                can_win = True
            else:
                # Противник выигрывает
                can_lose = True

    if can_win:
        return 'W'
    else:
        return 'L'

print("=" * 60)
print("УНИВЕРСАЛЬНЫЙ АНАЛИЗ ТЕОРИИ ИГР")
print("=" * 60)
print(f"\nФиниш: >= {FINISH} камней")
print("Ходы: +1, +3, *2\n")

# Анализируем позиции
results = {}
for s in range(1, FINISH):
    # Проверяем разные глубины
    results[s] = {
        'depth_1': analyze_position(s, 1),  # Один ход
        'depth_2': analyze_position(s, 2),  # Два хода
        'depth_3': analyze_position(s, 3),  # Три хода
    }

# ЗАДАЧА 19: Петя выигрывает первым ходом
task19 = [s for s in range(1, FINISH) if results[s]['depth_1'] == 'W']
print("ЗАДАЧА 19 (Петя выигрывает 1-м ходом):")
print(f"  S = {task19}")
print(f"  Наименьшее: {min(task19) if task19 else 'нет'}")

# ЗАДАЧА 20: Ваня выигрывает первым ходом
# Это позиции, где Петя НЕ может выиграть за 1 ход,
# но Петя может сделать ход, после которого Ваня выигрывает за 1 ход
task20 = []
for s in range(1, FINISH):
    if s in task19:
        continue

    # Проверяем, что все ходы Пети ведут к позициям, где Ваня выигрывает
    moves = get_moves(s)
    all_lead_to_vanya_win = True

    for move in moves:
        if move >= FINISH:
            all_lead_to_vanya_win = False
            break

        if results[move]['depth_1'] != 'W':
            all_lead_to_vanya_win = False
            break

    if all_lead_to_vanya_win:
        task20.append(s)

print("\nЗАДАЧА 20 (Ваня выигрывает 1-м ходом):")
print(f"  S = {task20}")

# ЗАДАЧА 21: Петя выигрывает вторым ходом
task21 = []
for s in range(1, FINISH):
    if s in task19 or s in task20:
        continue

    # Проверяем, что у Пети есть ход в позицию из task20
    moves = get_moves(s)

    has_good_move = False
    for move in moves:
        if move >= FINISH:
            continue
        if move in task20:
            has_good_move = True
            break

    if has_good_move:
        task21.append(s)

print("\nЗАДАЧА 21 (Петя выигрывает 2-м ходом):")
print(f"  S = {task21}")

# Подробный анализ для нескольких значений
print("\n" + "=" * 60)
print("ПОДРОБНЫЙ АНАЛИЗ (первые позиции):")
print("=" * 60)

for s in range(max(1, FINISH - 15), FINISH):
    status = "?"
    if s in task19:
        status = "П1 (Петя, 1-й ход)"
    elif s in task20:
        status = "В1 (Ваня, 1-й ход)"
    elif s in task21:
        status = "П2 (Петя, 2-й ход)"

    moves = get_moves(s)
    print(f"S={s:2d}: {status:20s} -> ходы: {moves}")
