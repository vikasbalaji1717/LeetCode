from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        # Build graph using only online nodes
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        costs = []

        for u, v, cost in edges:
            if online[u] and online[v]:
                graph[u].append((v, cost))
                indegree[v] += 1
                costs.append(cost)

        # Topological sort
        q = deque()

        for i in range(n):
            if online[i] and indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei, cost in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # Candidate scores
        costs = sorted(set(costs))

        # Check whether score X is achievable
        def canAchieve(score):
            INF = float('inf')
            dp = [INF] * n
            dp[0] = 0

            for node in topo:
                if dp[node] == INF:
                    continue

                for nei, cost in graph[node]:
                    if cost >= score:
                        new_cost = dp[node] + cost

                        if new_cost < dp[nei]:
                            dp[nei] = new_cost

            return dp[n - 1] <= k

        # Binary search maximum achievable score
        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            score = costs[mid]

            if canAchieve(score):
                ans = score
                left = mid + 1
            else:
                right = mid - 1

        return ans