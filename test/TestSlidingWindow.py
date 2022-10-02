import unittest

from algos.SlidingWindow import SlidingWindow


class TestSlidingWindow(unittest.TestCase):

    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4

    def test_sliding_window(self):
        algo1 = SlidingWindow()
        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        algo1.sliding_window(lst, 3)

    def test_max_sum_v1(self):
        algo2 = SlidingWindow()
        algo2.max_sum_v1(self.arr, self.k)

    def test_max_sum_v2(self):
        algo3 = SlidingWindow()
        algo3.max_sum_v2(self.arr, self.k)


if __name__ == '__main__':
    unittest.main()
