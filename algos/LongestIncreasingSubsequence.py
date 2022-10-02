class LongestIncreasingSubsequence:
    global maximum

    def _lis(self, arr, n):

        # to allow the access of global variable
        global maximum

        # Base Case
        if n == 1:
            return 1

        # maxEndingHere is the length of LIS ending with arr[n-1]
        maxEndingHere = 1

        """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
           IF arr[i-1] is smaller than arr[n-1], and max ending with
           arr[n-1] needs to be updated, then update it"""
        for i in range(1, n):
            res = self._lis(arr, i)
            if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
                maxEndingHere = res + 1

        # Compare maxEndingHere with overall maximum. And
        # update the overall maximum if needed
        maximum = max(maximum, maxEndingHere)

        return maxEndingHere

    def lis(self, arr):

        # to allow the access of global variable
        global maximum

        # length of arr
        n = len(arr)

        # maximum variable holds the result
        maximum = 1

        # The function _lis() stores its result in maximum
        self._lis(arr, n)

        return maximum

    def increase(X):
        return X + 1

    # N = 5, A = [3, 4, 4, 6, 1, 4, 4]
    # def solution(self, N, A):
    #     final_counter_arr = [0] * N
    #     counter = 0
    #     for K in range(1, N):
    #
    #         if (A[K] == N + 1 and N >= 1):
    #             max_counter = max(final_counter_arr)
    #             final_counter_arr.append(max_counter)
    #
    #         elif A[K] <= N and A[K] >= 1:
    #             counter = counter + 1
    #             final_counter_arr.append(counter)
    #     return final_counter_arr

    def solution(self, N, A):
        result = [0] * N  # The list to be returned
        max_counter = 0  # The used value in previous max_counter command
        current_max = 0  # The current maximum value of any counter
        for command in A:
            if 1 <= command <= N:
                res = result[command - 1]
                # increase(X) command
                if max_counter > res:
                    # lazy write
                    result[command - 1] = max_counter
                result[command - 1] += 1
                if current_max < result[command - 1]:
                    current_max = result[command - 1]
            else:
                # max_counter command
                # just record the current maximum value for later write
                max_counter = current_max
        for index in range(0, N):
            if result[index] < max_counter:
                # This element has never been used/updated after previous
                #     max_counter command
                result[index] = max_counter
        return result

