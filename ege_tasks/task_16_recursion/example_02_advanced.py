"""
ЗАДАЧА 16 - Рекурсия (сложнее)

Условие:
def F(n):
    if n > 0:
        return F(n - 1) + 2 * G(n - 1)
    else:
        return 1

def G(n):
    if n > 0:
        return F(n - 1) + G(n - 1)
    else:
        return 1

Чему равна сумма F(5) + G(5)?
"""

# Решение с мемоизацией (чтобы не пересчитывать)
memo_f = {}
memo_g = {}

def F(n):
    if n in memo_f:
        return memo_f[n]

    if n > 0:
        result = F(n - 1) + 2 * G(n - 1)
    else:
        result = 1

    memo_f[n] = result
    return result

def G(n):
    if n in memo_g:
        return memo_g[n]

    if n > 0:
        result = F(n - 1) + G(n - 1)
    else:
        result = 1

    memo_g[n] = result
    return result

# Вычисляем
print("Пошаговое вычисление:")
for i in range(6):
    f_val = F(i)
    g_val = G(i)
    print(f"F({i}) = {f_val}, G({i}) = {g_val}")

result = F(5) + G(5)
print(f"\nОтвет: F(5) + G(5) = {F(5)} + {G(5)} = {result}")
