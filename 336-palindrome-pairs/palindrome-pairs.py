
class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        result = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                left = word[:j]
                right = word[j:]

                # Case 1: left is a palindrome
                # Find a word that can be placed before word
                if is_palindrome(left):
                    needed = right[::-1]

                    if needed in word_map:
                        k = word_map[needed]

                        if k != i:
                            result.append([k, i])

                # Case 2: right is a palindrome
                # Find a word that can be placed after word
                # j < n avoids duplicate pairs in some cases
                if j < n and is_palindrome(right):
                    needed = left[::-1]

                    if needed in word_map:
                        k = word_map[needed]

                        if k != i:
                            result.append([i, k])

        return result
