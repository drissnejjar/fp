import unittest

from algos.LongestIncreasingSubsequence import LongestIncreasingSubsequence
from algos.SlidingWindow import SlidingWindow
from algos.TwoPointers import TwoPointers


class TestLongestIncreasingSubsequence(unittest.TestCase):

    arr = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]
    reversed_arr = arr[::-1]

    n = len(arr)

    A = [3, 4, 4, 6, 1, 4, 4]
    N = 5

    def test_lis(self):
        print(self.reversed_arr)
        lis = LongestIncreasingSubsequence()
        result = lis.lis(self.reversed_arr)
        print(result)

    def test_solution(self):
        lis = LongestIncreasingSubsequence()
        print(lis.solution(self.N, self.A))


if __name__ == '__main__':
    unittest.main()

