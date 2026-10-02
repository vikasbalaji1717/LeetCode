class Solution:
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):

                live = 0

                # Check 8 neighbors
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):

                        if x == i and y == j:
                            continue

                        # 1 and 2 both mean the cell was originally alive
                        if board[x][y] == 1 or board[x][y] == 2:
                            live += 1

                # Live cell
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2

                # Dead cell
                else:
                    if live == 3:
                        board[i][j] = 3

        # Convert temporary values
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1