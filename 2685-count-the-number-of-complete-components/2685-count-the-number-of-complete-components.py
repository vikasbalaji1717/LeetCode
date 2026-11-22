
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # Step 1: Create adjacency list
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        # Step 2: DFS function
        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        # Step 3: Find connected components
        for i in range(n):
            if not visited[i]:

                component = []
                dfs(i, component)

                # Step 4: Count edges
                total_nodes = len(component)

                total_edges = sum(
                    len(graph[node]) for node in component
                ) // 2

                # Step 5: Check if complete
                expected_edges = total_nodes * (total_nodes - 1) // 2

                if total_edges == expected_edges:
                    count += 1

        return count
