import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val):
        if val in self.index:
            return False

        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.index:
            return False

        idx = self.index[val]
        last = self.nums[-1]

        # Move last element into the position of val
        self.nums[idx] = last
        self.index[last] = idx

        # Remove last element
        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()