import sys


class SlidingWindow:

    def __init__(self):
        self.INT_MIN = -sys.maxsize - 1
    '''
     A sliding window is a subset of a data structure at a given point of time.
     The window size decides the number of elements in the subset.
     Function 1
    '''
    @staticmethod
    def sliding_window(elements, window_size):
        if len(elements) <= window_size:
            return elements
        for i in range(len(elements)):
            print(elements[i:i+window_size])

    '''Brute force approach We start with first index and sum till k-th element. We do it for all possible 
    consecutive blocks or groups of k elements. This method requires nested for loop, the outer for loop starts with 
    the starting element of the block of k elements and the inner or the nested loop will add up till the k-th 
    element. 
    Function 2 '''
    def max_sum_v1(self, arr, k):
        # Initialize result
        max_sum = self.INT_MIN
        n = len(arr)

        # Consider all blocks
        # starting with i.
        for i in range(n - k + 1):
            current_sum = 0
            for j in range(k):
                current_sum = current_sum + arr[i + j]

            # Update result if required.
            max_sum = max(current_sum, max_sum)
        print(max_sum)
        return max_sum

    @staticmethod
    def max_sum_v2(arr, k):
        # length of the array
        n = len(arr)

        # n must be greater than k
        if n < k:
            print("Invalid")
            return -1

        # Compute sum of first window of size k
        window_sum = sum(arr[:k])

        # first sum available
        max_sum = window_sum

        # Compute the sums of remaining windows by
        # removing first element of previous
        # window and adding last element of
        # the current window.
        for i in range(n - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(window_sum, max_sum)

        print(max_sum)
        return max_sum





