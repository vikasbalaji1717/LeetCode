
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != 'O'):
                return

            # Temporarily protect this O
            board[r][c] = '#'

            # Visit all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Protect O cells connected to the border
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Capture surrounded regions and restore protected cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
