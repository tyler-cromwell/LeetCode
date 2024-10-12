class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num not in d:
                d[num] = index # Never seen before
            elif abs(index - d[num]) <= k:
                return True
            else:
                d[num] = index # Store new index
        return False
