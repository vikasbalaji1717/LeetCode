class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False

        return len(stack) == 0