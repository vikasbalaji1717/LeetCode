
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        graph = defaultdict(list)

        # Build the adjacency list
        for start, end in tickets:
            graph[start].append(end)

        # Reverse sort so the smallest destination is popped first
        for airport in graph:
            graph[airport].sort(reverse=True)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]
