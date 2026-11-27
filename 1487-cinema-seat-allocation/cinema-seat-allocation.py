
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:

        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Seat block masks
        left = sum(1 << i for i in range(2, 6))
        middle = sum(1 << i for i in range(4, 8))
        right = sum(1 << i for i in range(6, 10))

        # All rows without reservations can fit 2 groups
        answer = (n - len(rows)) * 2

        # Check only rows with reserved seats
        for reserved in rows.values():

            left_free = (reserved & left) == 0
            middle_free = (reserved & middle) == 0
            right_free = (reserved & right) == 0

            if left_free and right_free:
                answer += 2

            elif left_free or middle_free or right_free:
                answer += 1

        return answer
