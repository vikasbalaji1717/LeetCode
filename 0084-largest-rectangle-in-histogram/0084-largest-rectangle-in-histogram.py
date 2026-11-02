class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = h * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area