
class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    result.append(path)
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == '0':
                    break

                current = int(num[index:i + 1])
                text = num[index:i + 1]

                if index == 0:
                    backtrack(i + 1, text, current, current)
                else:
                    # Addition
                    backtrack(
                        i + 1, path + "+" + text,
                        value + current, current
                    )

                    # Subtraction
                    backtrack(
                        i + 1, path + "-" + text,
                        value - current, -current
                    )

                    # Multiplication
                    backtrack(
                        i + 1, path + "*" + text,
                        value - last + last * current,
                        last * current
                    )

        backtrack(0, "", 0, 0)
        return result
