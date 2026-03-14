"""
Name: Bramesh Patel
Assignment: M3 – Analyze Running Times of Search Algorithms
Date: March 13, 2026

Description:
This program measures and compares the execution time of three search algorithms:
1. Recursive Binary Search
2. Iterative Binary Search
3. Sequential Search

Random arrays of increasing size are generated and sorted for binary search.
Each algorithm is executed 10 times for each data size and the average runtime
is calculated in microseconds using time.perf_counter().
"""


import random
import time

from search_algorithms import (
    recursive_binary_search,
    iterative_binary_search,
    sequential_search
)

# Data sizes required by the assignment
dataSize = [5000, 50000, 100000, 150000, 1000000]

for N in dataSize:

    SumRBS = 0
    SumIBS = 0
    SumSeqS = 0

    for _ in range(10):   # run experiment 10 times

        # generate sorted random list
        arr = sorted([random.randint(1, 1000000) for _ in range(N)])

        # random target
        target = random.randint(1, 1000000)

        # Recursive Binary Search
        start = time.perf_counter()
        recursive_binary_search(arr, target, 0, len(arr) - 1)
        SumRBS += (time.perf_counter() - start) * 1_000_000

        # Iterative Binary Search
        start = time.perf_counter()
        iterative_binary_search(arr, target)
        SumIBS += (time.perf_counter() - start) * 1_000_000

        # Sequential Search
        start = time.perf_counter()
        sequential_search(arr, target)
        SumSeqS += (time.perf_counter() - start) * 1_000_000

    print(f"\nN = {N}")
    print(f"Average Recursive Binary Search time: {SumRBS / 10:.2f} µs")
    print(f"Average Iterative Binary Search time: {SumIBS / 10:.2f} µs")
    print(f"Average Sequential Search time: {SumSeqS / 10:.2f} µs")