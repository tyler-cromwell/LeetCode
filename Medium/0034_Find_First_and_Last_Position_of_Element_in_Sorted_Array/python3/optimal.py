class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchRangeLeft(nums, target)
        right = self.searchRangeRight(nums, target)
        if left > right: return [-1,-1]
        else: return [left,right]

    def searchRangeLeft(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        if n == 0: return -1
        while start <= end:
            mid = (end+start) // 2
            if target <= nums[mid]: end = mid-1
            else: start = mid+1

        return start

    def searchRangeRight(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1

        if n == 0: return -1
        while start <= end:
            mid = (end+start) // 2
            if target >= nums[mid]: start = mid+1
            else: end = mid-1

        return end
