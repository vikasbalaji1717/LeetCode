
class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:

        def get_max_subsequence(nums, length):
            stack = []
            drop = len(nums) - length

            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []
            i = j = 0

            while i < len(a) or j < len(b):
                if a[i:] > b[j:]:
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1

            return result

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            part1 = get_max_subsequence(nums1, i)
            part2 = get_max_subsequence(nums2, k - i)

            candidate = merge(part1, part2)

            if candidate > answer:
                answer = candidate

        return answer
