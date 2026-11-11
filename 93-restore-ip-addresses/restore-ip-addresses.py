
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        result = []

        def backtrack(index, parts):

            # We need exactly 4 sections
            if len(parts) == 4:
                if index == len(s):
                    result.append(".".join(parts))
                return

            # Try section lengths 1, 2, and 3
            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

                # No leading zeros
                if len(part) > 1 and part[0] == '0':
                    break

                # Value must be between 0 and 255
                if int(part) > 255:
                    continue

                parts.append(part)

                backtrack(index + length, parts)

                # Backtrack
                parts.pop()

        backtrack(0, [])

        return result
