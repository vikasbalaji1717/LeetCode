
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        word_set = set(wordDict)

        @lru_cache(None)
        def backtrack(start):

            # Entire string has been used
            if start == len(s):
                return [""]

            result = []

            # Try every possible next word
            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in word_set:

                    remaining = backtrack(end)

                    for sentence in remaining:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            return result

        return backtrack(0)
