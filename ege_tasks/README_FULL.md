# ПОЛНЫЙ ГАЙД ПО ЗАДАЧАМ ЕГЭ 🔥

## База (Изи забираем баллы в пару строк)

### ✅ Задача 2 - Таблицы истинности
**Что нужно:** `itertools.product`

Перебираем все комбинации 0/1 для переменных и проверяем условие.

```python
from itertools import product
count = sum(1 for x, y, z in product([0, 1], repeat=3) if (x or y) and z)
```

**Примеры:**
- `task_02_truth_tables/example_01.py` - базовая таблица истинности
- `task_02_truth_tables/example_02.py` - импликация и сложные условия

---

### ✅ Задача 5 - Системы счисления
**Что нужно:** `int(число, основание)`

Переводим числа из разных систем и считаем.

```python
left = int('10110', 2)   # Двоичная
right = int('101', 8)    # Восьмеричная
count = right - left + 1
```

**Примеры:**
- `task_05_systems/example_01.py` - простой диапазон
- `task_05_systems/example_02.py` - с делимостью

---

### ✅ Задача 8 - Комбинаторика
**Что нужно:** `itertools.permutations`, `itertools.product`

Перестановки и размещения с повторениями/без.

```python
from itertools import permutations
for perm in permutations([1, 2, 3, 4, 5]):
    number = perm[0]*10000 + perm[1]*1000 + ...
```

**Примеры:**
- `task_08_combinatorics/example_01.py` - без повторений
- `task_08_combinatorics/example_02.py` - с повторениями

---

### ✅ Задача 12 - Редактор строк
**Что нужно:** `.replace()`, циклы `while`

Алгоритм замены подстрок по правилам.

```python
while "01" in s or "02" in s:
    s = s.replace("01", "2302")
    s = s.replace("02", "10")
```

**Примеры:**
- `task_12_string_editor/example_01.py` - базовые замены
- `task_12_string_editor/example_02.py` - сложные правила

---

### ✅ Задача 14 - Системы счисления (уравнения)
**Что нужно:** перевод в 10-ю систему, перебор

Ищем основание системы или считаем цифры.

```python
def to_base(num, base):
    # перевод в систему с основанием base
```

**Примеры:**
- `task_14_number_systems/example_01.py` - подсчёт цифр
- `task_14_number_systems/example_02.py` - поиск основания

---

### ✅ Задача 15 - Логика и побитовые операции
**Что нужно:** импликация, перебор

```python
def implies(a, b):
    return (not a) or b
```

**Примеры:**
- `task_15_logic/example_01.py` - делимость
- `task_15_logic/example_02.py` - отрезки на прямой

---

## Мидл (Подключаем модули и массивы)

### 🚀 Задача 13 - IP-адреса
**Что нужно:** `ipaddress` модуль

```python
import ipaddress
network = ipaddress.IPv4Network("192.168.32.160/27", strict=False)
print(network.netmask)
```

**Примеры:**
- `task_13_ip_addresses/example_01.py` - маска подсети
- `task_13_ip_addresses/example_02.py` - количество единиц

---

### 🚀 Задача 16 - Рекурсия
**Что нужно:** `functools.lru_cache`, `sys.setrecursionlimit`

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def F(n):
    if n <= 2:
        return n
    return F(n-1) + F(n-2)
```

**Примеры:**
- `task_16_recursion/example_01.py` - простая рекурсия
- `task_16_recursion/example_02_advanced.py` - взаимная рекурсия

---

### 🚀 Задача 17 - Последовательности
**Что нужно:** работа с файлами, вложенные циклы

```python
with open('numbers.txt', 'r') as f:
    numbers = [int(line) for line in f]

# Ищем пары
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        # проверяем условия
```

**Примеры:**
- `task_17_sequences/example_01.py` - пары элементов
- `task_17_sequences/example_02_with_file.py` - соседние элементы

---

### 🚀 Задача 23 - Динамическое программирование
**Что нужно:** рекурсия + мемоизация или DP таблица

```python
dp = [0] * (finish + 1)
dp[start] = 1

for i in range(start, finish):
    dp[i+1] += dp[i]
    dp[i+2] += dp[i]
    dp[i*2] += dp[i]
```

**Примеры:**
- `task_23_dynamic/example_01.py` - подсчёт путей
- `task_23_dynamic/example_02_with_restrictions.py` - с ограничениями

---

## Теория игр (Уничтожаем кучи камней) 🎮

### 🎯 Задачи 19, 20, 21 - Петя и Ваня
**УНИВЕРСАЛЬНЫЙ ШАБЛОН с @lru_cache!**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def can_win(stones, is_petya_turn):
    if stones >= FINISH:
        return False

    for move in get_moves(stones):
        if move >= FINISH:
            return True
        if not can_win(move, not is_petya_turn):
            return True

    return False
```

**Примеры:**
- `task_19_20_21_game_theory/example_01.py` - базовая игра
- `task_19_20_21_game_theory/example_02_advanced.py` - универсальный шаблон

---

## Хард (Файлы, алгоритмы и оптимизация) 💀

### 🔥 Задача 24 - Обработка текстовых файлов
**Что нужно:** чтение файлов, поиск подстрок

```python
with open('file.txt', 'r') as f:
    text = f.read()

# Ищем паттерны
max_length = 0
current_length = 1

for i in range(1, len(text)):
    if text[i] == text[i-1]:
        # обработка
```

**Примеры:**
- `task_24_string_files/example_01.py` - поиск без повторов
- `task_24_string_files/example_02_complex.py` - сложный паттерн C...B...A

---

### 🔥 Задача 25 - Делители и маски
**Что нужно:** оптимизация поиска делителей

```python
def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count
```

**Примеры:**
- `task_25_divisors/example_01.py` - поиск чисел с N делителями
- `task_25_divisors/example_02.py` - нечётные делители

---

### 🔥 Задача 26 - Жадные алгоритмы
**Что нужно:** сортировка, жадные алгоритмы

```python
weights_sorted = sorted(weights)
shelves = [0] * k

for weight in weights_sorted:
    # ищем лучший стеллаж
```

**Примеры:**
- `task_26_sorting/example_01.py` - размещение товаров

---

### 🔥 Задача 27 - Сложная оптимизация
**Два файла:**
- **Файл А (малый):** простой перебор O(N²)
- **Файл Б (большой):** оптимизация O(N) через группировку

```python
# Файл А
for i in range(n):
    for j in range(i+1, n):
        if condition:
            # считаем

# Файл Б - группируем по остатку
groups = {0: [], 1: [], 2: []}
for i, num in enumerate(numbers):
    groups[i % 3].append(num)
```

**Примеры:**
- `task_27_optimization/example_01.py` - файл А (перебор)
- `task_27_optimization/example_02_optimized.py` - файл Б (оптимизация)

---

## Быстрая шпаргалка

### Импорты для ЕГЭ
```python
from itertools import product, permutations, combinations
from functools import lru_cache
import ipaddress
import sys
```

### Частые паттерны
```python
# Таблицы истинности
for x, y, z in product([0, 1], repeat=3):
    if условие: count += 1

# Рекурсия
@lru_cache(maxsize=None)
def F(n):
    # база + рекурсия

# Делители
i = 1
while i * i <= n:
    if n % i == 0:
        # i и n//i - делители
    i += 1

# Динамика
dp = [0] * (n + 1)
dp[start] = 1
for i in range(start, n):
    # переходы
```

---

## Рекомендуемый порядок изучения

**Неделя 1-2: База**
1. Задача 5 (системы счисления)
2. Задача 2 (таблицы истинности)
3. Задача 8 (комбинаторика)
4. Задача 12 (редактор строк)

**Неделя 3-4: Мидл**
5. Задача 16 (рекурсия)
6. Задача 17 (последовательности)
7. Задача 13 (IP-адреса)
8. Задача 14, 15 (системы и логика)

**Неделя 5-6: Теория игр и DP**
9. Задача 23 (динамика)
10. Задачи 19, 20, 21 (теория игр)

**Неделя 7-8: Хард**
11. Задача 25 (делители)
12. Задача 24 (файлы)
13. Задача 26 (жадные алгоритмы)
14. Задача 27 (оптимизация)

---

## Полезные ссылки
- Все примеры с решениями в папках `task_XX_*/`
- Шпаргалка: `CHEATSHEET.md`
- Упражнения: `practice/exercises.py`
- Шаблон: `practice/template.py`

**УДАЧИ НА ЕГЭ! ТЫ УНИЧТОЖИШЬ ЭТИ ЗАДАЧИ!** 🔥💪
