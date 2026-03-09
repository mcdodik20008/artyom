# 📝 Шпаргалка по Python для ЕГЭ

## 🔢 Системы счисления

```python
# Перевод из других систем в десятичную
binary = int('1010', 2)      # Двоичная (2-я система)
octal = int('752', 8)        # Восьмеричная (8-я система)
hex_num = int('1A3F', 16)    # Шестнадцатеричная (16-я система)

# Перевод из десятичной в другие системы
bin(42)   # '0b101010' - двоичная
oct(42)   # '0o52' - восьмеричная
hex(42)   # '0x2a' - шестнадцатеричная

# Получить строку без префикса
bin(42)[2:]  # '101010'
oct(42)[2:]  # '52'
hex(42)[2:]  # '2a'
```

## 🔁 Циклы и диапазоны

```python
# Цикл от 1 до 10 (включительно)
for i in range(1, 11):
    print(i)

# Цикл от 0 до 9
for i in range(10):
    print(i)

# Цикл с шагом
for i in range(0, 20, 2):  # Чётные числа от 0 до 18
    print(i)

# Цикл в обратном порядке
for i in range(10, 0, -1):  # От 10 до 1
    print(i)
```

## 📋 Списки и работа с ними

```python
# Создание списка
numbers = [1, 2, 3, 4, 5]

# Генератор списков (list comprehension)
squares = [x**2 for x in range(1, 11)]  # [1, 4, 9, 16, ..., 100]

# Фильтрация
evens = [x for x in range(1, 21) if x % 2 == 0]

# Сумма, минимум, максимум
total = sum(numbers)
minimum = min(numbers)
maximum = max(numbers)

# Длина списка
length = len(numbers)

# Перебор элементов с индексами
for i, value in enumerate(numbers):
    print(f"Индекс {i}: значение {value}")
```

## 📂 Работа с файлами

```python
# Чтение всего файла
with open('file.txt', 'r') as f:
    content = f.read()

# Чтение построчно
with open('file.txt', 'r') as f:
    lines = f.readlines()  # Список строк

# Чтение чисел из файла (по одному в строке)
with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

# Запись в файл
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write(str(42))
```

## 🔍 Делители чисел

```python
# Найти все делители числа n
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# Подсчёт количества делителей
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

# Проверка на простое число
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

## 🔄 Рекурсия

```python
# Простая рекурсивная функция
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Числа Фибоначчи
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# С мемоизацией (для оптимизации)
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]
```

## 🔢 Полезные математические операции

```python
# Деление с остатком
quotient = 17 // 5   # 3 (целая часть)
remainder = 17 % 5   # 2 (остаток)

# Возведение в степень
result = 2 ** 10     # 1024

# Квадратный корень
import math
sqrt = math.sqrt(16)  # 4.0

# Или без import:
sqrt = 16 ** 0.5

# Округление
round(3.7)      # 4
math.floor(3.7)  # 3
math.ceil(3.2)   # 4

# Абсолютное значение
abs(-42)        # 42
```

## 🎯 Полезные приёмы

```python
# Проверка цифр в числе
str_num = str(12345)
if '3' in str_num:
    print("Число содержит цифру 3")

# Последняя цифра числа
last_digit = 12345 % 10  # 5

# Сумма цифр числа
digit_sum = sum(int(d) for d in str(12345))  # 15

# Количество цифр
digit_count = len(str(12345))  # 5

# Проверка на чётность
is_even = (num % 2 == 0)
is_odd = (num % 2 == 1)

# Все комбинации (пары)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # arr[i] и arr[j] - пара элементов
        pass

# Соседние элементы
for i in range(len(arr) - 1):
    # arr[i] и arr[i+1] - соседи
    pass
```

## ⚡ Оптимизация

```python
# Вместо:
count = 0
for x in range(a, b + 1):
    count += 1

# Используй:
count = b - a + 1

# Вместо проверки всех чисел до n:
for i in range(2, int(n**0.5) + 1):  # Только до корня
    # ...

# Для делимости на 3 в диапазоне:
# Первое число >= a, делящееся на 3
first = a + (3 - a % 3) % 3
# Последнее число <= b, делящееся на 3
last = b - b % 3
# Количество
count = (last - first) // 3 + 1
```

## 🎓 Частые ошибки

```python
# ❌ НЕПРАВИЛЬНО
range(1, 10)  # НЕ включает 10! (от 1 до 9)

# ✅ ПРАВИЛЬНО
range(1, 11)  # Включает 10 (от 1 до 10)

# ❌ НЕПРАВИЛЬНО
if n % 2 == 0 or 3:  # Неправильная логика!

# ✅ ПРАВИЛЬНО
if n % 2 == 0 or n % 3 == 0:

# ❌ НЕПРАВИЛЬНО (деление)
5 / 2   # = 2.5 (вещественное деление)

# ✅ ПРАВИЛЬНО (целочисленное)
5 // 2  # = 2 (целая часть)
```

---

💡 **Совет**: Держи эту шпаргалку под рукой во время решения задач!
