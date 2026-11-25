
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        nxt = [{}]
        link = [-1]
        length = [0]
        occ = [0]

        last = 0

        # Build suffix automaton
        for x in nums:
            cur = len(nxt)

            nxt.append({})
            link.append(0)
            length.append(length[last] + 1)
            occ.append(1)

            p = last

            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nxt)

                    nxt.append(nxt[q].copy())
                    link.append(link[q])
                    length.append(length[p] + 1)
                    occ.append(0)

                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        # Sort states by length using counting sort
        m = len(nxt)
        cnt = [0] * (len(nums) + 1)

        for l in length:
            cnt[l] += 1

        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]

        order = [0] * m

        for v in range(m - 1, -1, -1):
            l = length[v]
            cnt[l] -= 1
            order[cnt[l]] = v

        # Calculate occurrence counts
        for v in reversed(order):
            if link[v] != -1:
                occ[link[v]] += occ[v]

        # Find shortest substring occurring exactly once
        ans = len(nums)

        for v in range(1, m):
            if occ[v] == 1:
                ans = min(ans, length[link[v]] + 1)

        return ans
