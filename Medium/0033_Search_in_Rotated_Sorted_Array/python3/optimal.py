class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Check if array is unshifted
        if nums[0] <= nums[n-1]:
            result = self._binarySearch(nums, 0, n-1, target)
            return result

        # Find index of the shift
        shift = -1
        leftMost = 0
        rightMost = n-1
        median = (leftMost+rightMost) // 2

        while leftMost < rightMost:
            median = (leftMost+rightMost) // 2
            if nums[leftMost] > nums[median]:
                # go left
                rightMost = median
            elif nums[median] > nums[rightMost]:
                # go right
                leftMost = median+1
            else:
                # leftMost is our base...?
                break

        base = leftMost
        start = 0
        end = n-1
        result = -1
        if nums[base] <= target and target <= nums[n-1]:
            # normal binary search on right-half
            result = self._binarySearch(nums, base, n-1, target)
        else:
            # normal binary search on left-half
            result = self._binarySearch(nums, 0, base-1, target)
        return result
    
    def _binarySearch(self, array: List[int], start: int, end: int, target: int) -> int:
        n = len(array)

        while start <= end:
            median = (start+end) // 2
            if array[median] == target:
                return median
            elif array[median] < target:
                start = median+1
            else:
                end = median-1

        return -1
