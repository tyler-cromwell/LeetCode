class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        windowSize = indexDiff+1

        # Base case
        if windowSize >= len(nums):
            for i in range(len(nums)):
                for j in range(len(nums)-1, i, -1):
                    #print(nums[i], nums[j], len(nums), i, j)
                    if abs(nums[i]-nums[j]) <= valueDiff:
                        return True
            return False

        # Grow the window
        #print('Growing')
        for i in range(1, windowSize):
            #print('_', nums[i], windowSize, '_', i)
            for j in range(i-1, 0-1, -1):
                #print('nums[{}] == nums[{}] -> {} == {}'.format(j, i, nums[j], nums[i]))
                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True

        # Slide the Window
        #print('Sliding')
        for i in range(windowSize, len(nums)):
            #print('_', nums[i], windowSize, '_', i)
            for j in range(i-1, i-windowSize, -1):
                #print('nums[{}] == nums[{}] -> {} == {}'.format(j, i, nums[j], nums[i]))
                if abs(nums[i]-nums[j]) <= valueDiff:
                    return True

        return False
