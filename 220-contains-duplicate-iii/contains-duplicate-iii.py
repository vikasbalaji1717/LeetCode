
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:

        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):

            # Remove elements outside the sliding window
            if i > indexDiff:
                old_num = nums[i - indexDiff - 1]
                old_bucket = old_num // bucket_size
                del buckets[old_bucket]

            bucket_id = num // bucket_size

            # Same bucket means value difference <= valueDiff
            if bucket_id in buckets:
                return True

            # Check the left neighboring bucket
            if bucket_id - 1 in buckets:
                if abs(num - buckets[bucket_id - 1]) <= valueDiff:
                    return True

            # Check the right neighboring bucket
            if bucket_id + 1 in buckets:
                if abs(num - buckets[bucket_id + 1]) <= valueDiff:
                    return True

            # Insert current number
            buckets[bucket_id] = num

        return False
