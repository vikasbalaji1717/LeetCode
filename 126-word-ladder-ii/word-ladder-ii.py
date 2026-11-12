
from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: list[str]) -> list[list[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Store all shortest parents of each word
        parents = defaultdict(set)

        queue = deque([beginWord])
        wordSet.discard(beginWord)

        found = False

        # BFS to find shortest paths
        while queue and not found:

            next_level = set()

            for _ in range(len(queue)):
                word = queue.popleft()
                chars = list(word)

                for i in range(len(chars)):
                    original = chars[i]

                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == original:
                            continue

                        chars[i] = ch
                        new_word = "".join(chars)

                        if new_word in wordSet:
                            parents[new_word].add(word)
                            next_level.add(new_word)

                            if new_word == endWord:
                                found = True

                    chars[i] = original

            # Remove words only after processing the whole level
            wordSet -= next_level
            queue.extend(next_level)

        if not found:
            return []

        # Backtracking to construct all shortest paths
        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        backtrack(endWord)

        return result
