class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                number = 0
                sign = 1

            elif ch == ')':
                result += sign * number
                number = 0

                sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + sign * result

        result += sign * number

        return result