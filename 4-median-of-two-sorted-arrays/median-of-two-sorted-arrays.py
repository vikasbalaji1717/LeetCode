
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            if i < m and j > 0 and B[j - 1] > A[i]:
                left = i + 1

            elif i > 0 and j < n and A[i - 1] > B[j]:
                right = i - 1

            else:
                max_left = max(
                    A[i - 1] if i > 0 else float("-inf"),
                    B[j - 1] if j > 0 else float("-inf")
                )

                if (m + n) % 2 == 1:
                    return float(max_left)

                min_right = min(
                    A[i] if i < m else float("inf"),
                    B[j] if j < n else float("inf")
                )

                return (max_left + min_right) / 2

        return 0.0
