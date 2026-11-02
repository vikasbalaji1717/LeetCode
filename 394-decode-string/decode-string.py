class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        current_num = 0
        current_string = ""

        for ch in s:

            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            elif ch == '[':
                stack.append((current_string, current_num))

                current_string = ""
                current_num = 0

            elif ch == ']':
                previous_string, repeat = stack.pop()

                current_string = (
                    previous_string +
                    current_string * repeat
                )

            else:
                current_string += ch

        return current_string