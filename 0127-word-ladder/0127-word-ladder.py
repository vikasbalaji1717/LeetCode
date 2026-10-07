from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        # endWord must be present in the dictionary
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            # Change every character
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))

        return 0