
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Find the next greater element for every index
        next_greater = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = i

            stack.append(i)

        # Cost of each complete segment
        segment_cost = [0] * n

        for i in range(n):
            nxt = next_greater[i]

            if nxt != -1:
                segment_cost[i] = (
                    nums[i] * (nxt - i)
                    - (prefix[nxt] - prefix[i])
                )

        # Binary lifting tables
        LOG = n.bit_length()

        up = [next_greater]
        costs = [segment_cost]

        for _ in range(1, LOG):
            prev_up = up[-1]
            prev_cost = costs[-1]

            curr_up = [-1] * n
            curr_cost = [0] * n

            for i in range(n):
                mid = prev_up[i]

                if mid != -1:
                    curr_up[i] = prev_up[mid]
                    curr_cost[i] = (
                        prev_cost[i] + prev_cost[mid]
                    )

            up.append(curr_up)
            costs.append(curr_cost)

        # Calculate the operations needed for nums[left:right+1]
        def get_cost(left, right):

            total = 0
            cur = left

            for j in range(LOG - 1, -1, -1):
                nxt = up[j][cur]

                if nxt != -1 and nxt <= right:
                    total += costs[j][cur]
                    cur = nxt

            total += (
                nums[cur] * (right - cur + 1)
                - (prefix[right + 1] - prefix[cur])
            )

            return total

        # Sliding window
        left = 0
        answer = 0

        for right in range(n):

            while get_cost(left, right) > k:
                left += 1

            answer += right - left + 1

        return answer
