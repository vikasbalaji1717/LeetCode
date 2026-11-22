
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        count = [0] * (n + 1)
        digits = []

        # Count non-zero digits up to each position
        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))

            count[i + 1] = len(digits)

        # Build prefix arrays
        prefix_num = [0]
        prefix_sum = [0]
        power10 = [1]

        for d in digits:
            prefix_num.append(
                (prefix_num[-1] * 10 + d) % MOD
            )
            prefix_sum.append(prefix_sum[-1] + d)
            power10.append(power10[-1] * 10 % MOD)

        answer = []

        # Answer each query
        for l, r in queries:
            left = count[l]
            right = count[r + 1]

            length = right - left

            x = (
                prefix_num[right]
                - prefix_num[left] * power10[length]
            ) % MOD

            total = prefix_sum[right] - prefix_sum[left]

            answer.append((x * total) % MOD)

        return answer
