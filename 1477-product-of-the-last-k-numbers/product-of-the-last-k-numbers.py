
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:

        # If number is zero, reset prefix
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:

        # Check if zero exists in last k numbers
        if k >= len(self.prefix):
            return 0

        # Calculate product using prefix division
        return self.prefix[-1] // self.prefix[-k - 1]
