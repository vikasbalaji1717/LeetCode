
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diagonals1 = set()  # row - col
        diagonals2 = set()  # row + col

        count = 0

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if (col in cols or
                    row - col in diagonals1 or
                    row + col in diagonals2):
                    continue

                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        backtrack(0)
        return count
