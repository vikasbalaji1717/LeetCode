
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for i in range(rows):

            # Update histogram heights
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find largest rectangle in histogram
            stack = []

            for j in range(cols + 1):

                current_height = heights[j] if j < cols else 0

                while stack and heights[stack[-1]] > current_height:

                    height = heights[stack.pop()]

                    if stack:
                        width = j - stack[-1] - 1
                    else:
                        width = j

                    area = height * width
                    max_area = max(max_area, area)

                stack.append(j)

        return max_area
