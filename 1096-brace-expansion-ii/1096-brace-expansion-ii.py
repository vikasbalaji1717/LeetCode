class Solution:
    def braceExpansionII(self, expression: str):
        def union(a, b):
            return a | b

        def product(a, b):
            return {x + y for x in a for y in b}

        def parse():
            nonlocal i

            res = set()
            cur = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1

                elif expression[i] == '{':
                    i += 1
                    temp = parse()
                    cur = product(cur, temp)
                    i += 1  # skip '}'

                else:  # letter
                    cur = product(cur, {expression[i]})
                    i += 1

            res |= cur
            return res

        i = 0
        n = len(expression)
        return sorted(parse())