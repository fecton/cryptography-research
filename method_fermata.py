"""
Предмет: Теоретичні основи криптології
Тема: Дослідження алгоритмів визначення простоти числа
Автор: Литвиненко А.В. 525а

Опис алгоритму:
Метод Ферма полягає в перевірці простоти числа за допомогою малої теореми Ферма, яка стверджує, що якщо p є простим числом і a є цілим числом, не ділиться націло на p, то a^(p-1) ≡ 1 (mod p). Цей метод не є 100% точним, але його точність збільшується зі зростанням кількості ітерацій.
"""

import random

def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Приклад використання функції:
number = 17
if is_prime_fermat(number):
    print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")
