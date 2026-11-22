
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:

        digits = "123456789"
        result = []

        # Generate different lengths
        for length in range(2, 10):

            # Take consecutive digits
            for i in range(10 - length):

                num = int(digits[i:i + length])

                # Check the given range
                if low <= num <= high:
                    result.append(num)

        return sorted(result)
