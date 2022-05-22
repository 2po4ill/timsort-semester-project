import unittest

from random import randint

from src.TimSort import tim_sort as ts
from src.MergeSort import merge as ms


class TestTimSort(unittest.TestCase):

    def test_sort_timsort(self):
        """ Testing timsort using comparison of neighboring elements """
        arr = []
        n = len(arr)
        for i in range(1000000):
            arr.append(randint(-100000, 100000))
        ts(arr)
        flag_check = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                flag_check = False
        self.assertIs(flag_check, True)
        self.assertEqual(n, 1000000)

    def test_builtin_sort_timsort(self):
        """ Testing timsort using the built-in sorting """
        arr = []
        n = len(arr)
        for i in range(1000000):
            arr.append(randint(-100000, 100000))
        s = arr.copy()
        ts(arr)
        s.sort()
        flag_check = True
        for i in range(n):
            if arr[i] != s[i]:
                flag_check = False
        self.assertIs(flag_check, True)

    def test_sort_merge(self):
        """ Testing mergesort using comparison of neighboring elements """
        arr = []
        for i in range(1000000):
            arr.append(randint(-100000, 100000))
        ms(arr)
        n = len(arr)
        flag_check = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                flag_check = False
        self.assertIs(flag_check, True)
        self.assertEqual(n, 1000000)

    def test_builtin_sort_mergesort(self):
        """ Testing mergesort using the built-in sorting """
        arr = []
        n = len(arr)
        for i in range(1000000):
            arr.append(randint(-100000, 100000))
        s = arr.copy()
        ms(arr)
        s.sort()
        flag_check = True
        for i in range(n):
            if arr[i] != s[i]:
                flag_check = False
        self.assertIs(flag_check, True)


if __name__ == '__main__':
    unittest.main()
