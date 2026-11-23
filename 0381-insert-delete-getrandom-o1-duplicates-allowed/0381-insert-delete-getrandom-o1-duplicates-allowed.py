
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        not_present = val not in self.indices

        if not_present:
            self.indices[val] = set()

        self.indices[val].add(len(self.nums))
        self.nums.append(val)

        return not_present

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        remove_idx = self.indices[val].pop()

        last_val = self.nums[-1]
        last_idx = len(self.nums) - 1

        self.nums[remove_idx] = last_val

        self.indices[last_val].add(remove_idx)
        self.indices[last_val].discard(last_idx)

        self.nums.pop()

        if not self.indices[val]:
            del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
