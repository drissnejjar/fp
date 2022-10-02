
class TwoPointers:

    '''
    Naïve approach to check if there is a pair
    '''
    def is_pair_sum_v1(self, A, N, X):

        for i in range(N):
            for j in range(N):

                # as equal i and j means same element
                if (i == j):
                    continue

                # pair exists
                print(f'IsEqual Element {i}: {A[i]} + Element {j}: {A[j]} == {X} => {A[i] + A[j] == X}')
                if (A[i] + A[j] == X):
                    return True

                print(f'IsGreater Element {i}: {A[i]} + Element {j}: {A[j]} > {X} => {A[i] + A[j] > X}')
                # as the array is sorted
                if (A[i] + A[j] > X):
                    break

        # No pair found with given sum
        return

    '''
    Naive approach to check if there is a pair using two pointers technique
    '''

    def is_pair_sum_v2(self, A, N, X):

        # represents first pointer
        i = 0

        # represents second pointer
        j = N - 1

        while (i < j):

            # If we find a pair
            if (A[i] + A[j] == X):
                return True

            # If sum of elements at current
            # pointers is less, we move towards
            # higher values by doing i += 1
            elif (A[i] + A[j] < X):
                i += 1

            # If sum of elements at current
            # pointers is more, we move towards
            # lower values by doing j -= 1
            else:
                j -= 1
        return 0


    def solution(self, A):
        smallest_pos_numb = 1
        N = len(A)
        A.sort()
        i = 0
        j = N
        if (max(A) < 0):
            return smallest_pos_numb
        else:
            while (i < j):
                if (A[i] + 1 in A):
                    i += 1
                else:
                    print(A[i] + 1)
                    return A[i] + 1

    # [-1, 6, 3, 4, 7, 4]
    def solution(self, A):
        inversion_counter = 0
        if (inversion_counter > 1000000000):
            inversion_counter = 1
            return inversion_counter
        N = len(A) - 1
        i = 0
        j = i + 1
        while i < j:
            if j < N:
                if A[i] > A[j]:
                    inversion_counter += 1
                    j += 1
                elif A[i] <= A[j]:
                    j += 1
                else:
                    i += 1
                    j = i + 1
            elif j == N and N - i > 1:
                i += 1
                j = i + 1
                if A[i] > A[j]:
                    inversion_counter += 1
                else:
                    pass
                pass
            elif j == N and N - i == 1:
                break
        return inversion_counter

