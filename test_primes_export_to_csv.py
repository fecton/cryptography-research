"""
Предмет: Теоретичні основи криптології
Тема: Дослідження алгоритмів визначення простоти числа
Автор: Литвиненко А.В. 525а

Опис програми: тестування усіх алгоритмів та збереження даних у csv-файл
"""

import time
import csv
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

numbers_to_test = list(range(2,102)) + list(range(202, 302)) + list(range(100002, 100102))

# Відкрити CSV-файл для запису результатів
with open("prime_test_results.csv", "w", newline="") as csvfile:
    fieldnames = ["Method", "Number", "Status", "Execution Time"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for name, test in prime_tests:
        print(f"Testing with {name} method:")
        total_time = 0

        for num in numbers_to_test:
            start_time = time.perf_counter()
            result = test(num)
            end_time = time.perf_counter()

            elapsed_time = end_time - start_time
            total_time += elapsed_time

            status = "prime" if result else "not prime"
            print(f"{num} is {status}, tested in {elapsed_time:.10f} seconds")

            # Записати результати у CSV-файл
            writer.writerow(
                {
                    "Method": name,
                    "Number": num,
                    "Status": status,
                    "Execution Time": elapsed_time,
                }
            )

        print(f"Total time for {name}: {total_time:.10f} seconds")
        print("-" * 40)
