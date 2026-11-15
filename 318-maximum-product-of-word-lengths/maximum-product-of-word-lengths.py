
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = []

        # Convert each word into a bitmask
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks.append(mask)

        max_product = 0

        # Compare every pair of words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)

        return max_product
