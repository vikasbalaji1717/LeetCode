class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0  # 0=N, 1=E, 2=S, 3=W

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for ch in instructions:
            if ch == 'G':
                dx, dy = dirs[direction]
                x += dx
                y += dy
            elif ch == 'L':
                direction = (direction - 1) % 4
            else:  # 'R'
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0
        