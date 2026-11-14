
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'

        s = s.replace(" ", "")

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:

                if op == '+':
                    stack.append(num)

                elif op == '-':
                    stack.append(-num)

                elif op == '*':
                    stack.append(stack.pop() * num)

                elif op == '/':
                    prev = stack.pop()
                    result = abs(prev) // num

                    if prev < 0:
                        result = -result

                    stack.append(result)

                op = ch
                num = 0

        return sum(stack)
