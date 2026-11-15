
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n - 1):
            first = num[:i]

            # First number cannot have leading zeros
            if len(first) > 1 and first[0] == '0':
                break

            for j in range(i + 1, n):
                second = num[i:j]

                # Second number cannot have leading zeros
                if len(second) > 1 and second[0] == '0':
                    break

                a = int(first)
                b = int(second)
                k = j

                while k < n:
                    total = str(a + b)

                    if not num.startswith(total, k):
                        break

                    k += len(total)
                    a, b = b, int(total)

                if k == n:
                    return True

        return False
