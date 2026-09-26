class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        m, n = len(matrix), len(matrix[0])

        # Find rows and columns containing 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Set rows to 0
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        # Set columns to 0
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0      