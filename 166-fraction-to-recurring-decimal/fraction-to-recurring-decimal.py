
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        # Determine the sign
        sign = "-" if (numerator < 0) != (denominator < 0) else ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        integer = numerator // denominator
        remainder = numerator % denominator

        result = sign + str(integer)

        if remainder == 0:
            return result

        result += "."

        # Store previously seen remainders
        seen = {}

        while remainder != 0:

            if remainder in seen:
                result = (
                    result[:seen[remainder]]
                    + "("
                    + result[seen[remainder]:]
                    + ")"
                )
                break

            seen[remainder] = len(result)

            remainder *= 10
            digit = remainder // denominator

            result += str(digit)
            remainder %= denominator

        return result
