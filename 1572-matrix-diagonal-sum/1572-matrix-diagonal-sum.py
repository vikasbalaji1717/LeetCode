class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]          # Primary diagonal
            total += mat[i][n - 1 - i]  # Secondary diagonal

        if n % 2 == 1:
            total -= mat[n // 2][n // 2]  # Remove center counted twice

        return total