class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board, words):

        # Build Trie
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word

        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):

            ch = board[r][c]

            # Character not present in Trie
            if ch not in node.children:
                return

            node = node.children[ch]

            # Found a complete word
            if node.word is not None:
                result.append(node.word)
                node.word = None   # Avoid duplicates

            # Mark current cell as visited
            board[r][c] = '#'

            # Four directions
            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)  # left
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != '#'):

                    dfs(nr, nc, node)

            # Backtrack
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result