"""Classic sorting and searching algorithms.

Sorting functions return a new list and never mutate the input sequence.
"""
from __future__ import annotations
from typing import TypeVar, Sequence

T = TypeVar("T")


def bubble_sort(values: Sequence[T]) -> list[T]:
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(values: Sequence[T]) -> list[T]:
    result = list(values)
    for start in range(len(result)):
        smallest = min(range(start, len(result)), key=result.__getitem__)
        result[start], result[smallest] = result[smallest], result[start]
    return result


def insertion_sort(values: Sequence[T]) -> list[T]:
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        cursor = index - 1
        while cursor >= 0 and result[cursor] > current:
            result[cursor + 1] = result[cursor]
            cursor -= 1
        result[cursor + 1] = current
    return result


def merge_sort(values: Sequence[T]) -> list[T]:
    items = list(values)
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    merged: list[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]


def quick_sort(values: Sequence[T]) -> list[T]:
    items = list(values)
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    lower = [item for item in items if item < pivot]
    equal = [item for item in items if item == pivot]
    greater = [item for item in items if item > pivot]
    return quick_sort(lower) + equal + quick_sort(greater)


def linear_search(values: Sequence[T], target: T) -> int:
    """Return the first matching index, or -1 when the target is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: Sequence[T], target: T) -> int:
    """Return the target index in a sorted sequence, or -1 if absent."""
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


SORTS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}
