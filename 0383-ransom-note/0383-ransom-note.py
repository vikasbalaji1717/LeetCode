class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        # Count letters in magazine
        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        # Use letters for ransomNote
        for ch in ransomNote:
            index = ord(ch) - ord('a')

            if count[index] == 0:
                return False

            count[index] -= 1

        return True