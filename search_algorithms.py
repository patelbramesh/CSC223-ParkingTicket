"""
Name: Bramesh Patel
Course: CSC 223 – Data Structures
Assignment: M3 – Analyze Running Times of Search Algorithms
Date: March 12, 2026

Description:
This program measures and compares the execution time of three search algorithms:
1. Recursive Binary Search
2. Iterative Binary Search
3. Sequential Search

Random arrays of increasing size are generated and sorted for binary search.
Each algorithm is executed 10 times for each data size and the average runtime
is calculated in microseconds using time.perf_counter().
"""


def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, high)


def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1
