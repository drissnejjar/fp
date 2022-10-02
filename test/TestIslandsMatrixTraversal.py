import unittest

from algos.IslandsMatrixTraversal import IslandsMatrixTraversal
from algos.SlidingWindow import SlidingWindow


class TestSlidingWindow(unittest.TestCase):
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]
    row = len(graph)
    col = len(graph[0])

    def test_islands(self):
        islands = IslandsMatrixTraversal(self.row, self.col, self.graph)
        islands.count_islands()


if __name__ == '__main__':
    unittest.main()
