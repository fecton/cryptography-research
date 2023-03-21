"""
Предмет: Теоретичні основи криптології
Тема: Дослідження алгоритмів визначення простоти числа
Автор: Литвиненко А.В. 525а

Опис алгоритму:
Метод Міллера-Рабіна - це статистичний тест простоти, який використовується для перевірки, чи є задане число простим. Його точність залежить від кількості ітерацій, але він вважається швидшим за метод грубої сити, особливо для великих чисел.
"""

import random

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Знайти r та d такі, що n-1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Приклад використання функції:
number = 17
if miller_rabin(number):
    print(f"{number} є простим числом")
else:
    print(f"{number} не є простим числом")
