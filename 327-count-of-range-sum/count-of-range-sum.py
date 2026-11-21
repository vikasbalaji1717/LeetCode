
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)

        def merge_sort(left, right):
            if right - left <= 1:
                return 0

            mid = (left + right) // 2

            count = merge_sort(left, mid)
            count += merge_sort(mid, right)

            j = k = mid

            for i in range(left, mid):
                while j < right and prefix[j] - prefix[i] < lower:
                    j += 1

                while k < right and prefix[k] - prefix[i] <= upper:
                    k += 1

                count += k - j

            # Merge the two sorted halves
            merged = []
            i, j = left, mid

            while i < mid and j < right:
                if prefix[i] <= prefix[j]:
                    merged.append(prefix[i])
                    i += 1
                else:
                    merged.append(prefix[j])
                    j += 1

            while i < mid:
                merged.append(prefix[i])
                i += 1

            while j < right:
                merged.append(prefix[j])
                j += 1

            prefix[left:right] = merged

            return count

        return merge_sort(0, len(prefix))
