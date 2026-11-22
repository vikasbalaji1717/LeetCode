
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        # Step 1: Sort nodes by their values
        order = sorted(range(n), key=lambda i: nums[i])
        values = [nums[i] for i in order]

        # Original node -> sorted position
        pos = [0] * n
        for i in range(n):
            pos[order[i]] = i

        # Step 2: Find connected components
        comp = [0] * n

        for i in range(1, n):
            comp[i] = comp[i - 1]

            if values[i] - values[i - 1] > maxDiff:
                comp[i] += 1

        # Step 3: Find farthest reachable position
        nxt = [0] * n
        j = 0

        for i in range(n):
            j = max(j, i)

            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1

            nxt[i] = j

        # Step 4: Build binary lifting table
        LOG = n.bit_length()

        up = [nxt]

        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[i]] for i in range(n)])

        # Step 5: Answer queries
        answer = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a == b:
                answer.append(0)
                continue

            if comp[a] != comp[b]:
                answer.append(-1)
                continue

            if a > b:
                a, b = b, a

            steps = 0

            # Take the largest jumps without passing b
            for k in range(LOG - 1, -1, -1):
                dest = up[k][a]

                if dest < b:
                    a = dest
                    steps += (1 << k)

            answer.append(steps + 1)

        return answer
