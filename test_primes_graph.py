"""
Предмет: Теоретичні основи криптології
Тема: Дослідження алгоритмів визначення простоти числа
Автор: Литвиненко А.В. 525а

Опис програми: тестування усіх алгоритмів та показ даних на графіку
"""

import time
import matplotlib.pyplot as plt
from brute_force import is_prime
from method_fermata import is_prime_fermat
from method_millera_rabina import miller_rabin
from method_aks import is_prime_aks

prime_tests = [
    ("Brute Force", is_prime),
    ("Fermat", is_prime_fermat),
    ("Miller-Rabin", miller_rabin),
    ("AKS", is_prime_aks),
]

# numbers_to_test = list(range(2, 102))
# numbers_to_test = list(range(202, 302))
numbers_to_test = list(range(100002, 100102))

# Зберігання результатів
results = []

for name, test in prime_tests:
    print(f"Testing with {name} method:")
    total_time = 0
    test_results = []

    for num in numbers_to_test:
        start_time = time.perf_counter()
        result = test(num)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        total_time += elapsed_time

        status = "prime" if result else "not prime"
        print(f"{num} is {status}, tested in {elapsed_time:.10f} seconds")

        test_results.append(elapsed_time)

    results.append(test_results)
    print(f"Total time for {name}: {total_time:.10f} seconds")
    print("-" * 40)

# Візуалізація результатів
fig, ax = plt.subplots()
bar_width = 0.2
opacity = 0.8

for index, (name, test_results) in enumerate(zip(prime_tests, results)):
    rects = ax.bar(
        [x + index * bar_width for x in range(len(numbers_to_test))],
        test_results,
        bar_width,
        alpha=opacity,
        label=name[0],
    )

ax.set_xlabel("Numbers")
ax.set_ylabel("Execution Time (s)")
ax.set_title("Execution Time of Prime Test Algorithms")
ax.set_xticks([x + 1.5 * bar_width for x in range(len(numbers_to_test))])
ax.set_xticklabels([str(x) for x in numbers_to_test])
ax.legend()

fig.tight_layout()
plt.show()