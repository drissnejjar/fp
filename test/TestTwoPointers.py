import unittest

from algos.SlidingWindow import SlidingWindow
from algos.TwoPointers import TwoPointers


class TestTwoPointers(unittest.TestCase):

    arr = [2, 3, 5, 8, 9, 10, 11]
    val = 15

    def test_is_pair_sum_v1(self):
        twoPointers = TwoPointers()
        twoPointers.is_pair_sum_v1(self.arr, len(self.arr), self.val)


    def test_is_pair_sum_v2(self):
        twoPointers = TwoPointers()
        result = twoPointers.is_pair_sum_v2(self.arr, len(self.arr), self.val)
        print(result)

    def test_solution(self):
        A =  [-1, 6, 3, 4, 7, 4]
        twoPointers = TwoPointers()
        twoPointers.solution(A)

if __name__ == '__main__':
    unittest.main()

