import unittest
from src.algorithms import (
    SORTS, binary_search, bubble_sort, insertion_sort, linear_search,
    merge_sort, quick_sort, selection_sort,
)


class SortingTests(unittest.TestCase):
    def test_every_sort_handles_mixed_values(self):
        values = [8, -2, 5, 5, 0, 11, 1]
        for name, algorithm in SORTS.items():
            with self.subTest(algorithm=name):
                self.assertEqual(algorithm(values), sorted(values))

    def test_sorts_do_not_mutate_input(self):
        values = [3, 1, 2]
        for algorithm in SORTS.values():
            algorithm(values)
            self.assertEqual(values, [3, 1, 2])

    def test_empty_and_single_item(self):
        for algorithm in SORTS.values():
            self.assertEqual(algorithm([]), [])
            self.assertEqual(algorithm([7]), [7])


class SearchingTests(unittest.TestCase):
    def test_linear_search_returns_first_match(self):
        self.assertEqual(linear_search([4, 2, 4], 4), 0)
        self.assertEqual(linear_search([4, 2, 4], 9), -1)

    def test_binary_search(self):
        self.assertEqual(binary_search([-5, 0, 4, 8, 12], 8), 3)
        self.assertEqual(binary_search([1, 3, 5], 2), -1)
        self.assertEqual(binary_search([], 1), -1)


if __name__ == "__main__":
    unittest.main()
