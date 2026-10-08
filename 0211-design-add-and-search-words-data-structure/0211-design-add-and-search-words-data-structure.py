class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()

            current = current.children[ch]

        current.is_end = True

    def search(self, word):
        def dfs(node, index):
            # Reached the end of the word
            if index == len(word):
                return node.is_end

            ch = word[index]

            # Normal character
            if ch != '.':
                if ch not in node.children:
                    return False

                return dfs(node.children[ch], index + 1)

            # '.' can match any character
            for child in node.children.values():
                if dfs(child, index + 1):
                    return True

            return False

        return dfs(self.root, 0)