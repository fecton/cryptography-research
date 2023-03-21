"""
Предмет: Теоретичні основи криптології
Тема: Дослідження алгоритмів визначення простоти числа
Автор: Литвиненко А.В. 525а

Опис алгоритму:
Метод АКС (Агравал-Каял-Саксена) - це детерміністичний тест простоти з поліноміальною складністю. Цей тест є теоретично важливим, але його практичне застосування обмежене через високу складність.
"""

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime_aks(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    r = 2
    while r < n:
        if gcd(n, r) != 1:
            return False
        q = n - 1
        while q % 2 == 0:
            q //= 2
        if pow(r, q, n) != 1:
            return False
        r += 1

    return True

# Приклад використання функції:
number = 17
if is_prime_aks(number):
    print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")
