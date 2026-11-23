
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # Make the number of rows the smaller dimension
        if m > n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m

        answer = float('-inf')

        for top in range(m):
            col_sum = [0] * n

            for bottom in range(top, m):

                # Compress rows into column sums
                for col in range(n):
                    col_sum[col] += matrix[bottom][col]

                # Find maximum subarray sum <= k
                prefix = 0
                sorted_prefix = [0]

                for value in col_sum:
                    prefix += value

                    target = prefix - k
                    index = bisect_left(sorted_prefix, target)

                    if index < len(sorted_prefix):
                        answer = max(
                            answer,
                            prefix - sorted_prefix[index]
                        )

                    insort(sorted_prefix, prefix)

                    if answer == k:
                        return k

        return answer
