from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def get_position(square):
            # Convert square number to row and column
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n

            # Every alternate row is reversed
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, moves = queue.popleft()

            if square == n * n:
                return moves

            # Try all possible dice rolls
            for dice in range(1, 7):
                next_square = square + dice

                if next_square > n * n:
                    break

                row, col = get_position(next_square)

                # Snake or ladder
                if board[row][col] != -1:
                    next_square = board[row][col]

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1