class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentNumber = 0
        pointer = 1
        duplicatesFound = 0
        
        while pointer < len(nums):
            if nums[pointer] == nums[currentNumber]:
                nums[pointer] = -999
                duplicatesFound = duplicatesFound + 1
            else:
                if duplicatesFound > 0:
                    nums[currentNumber+1] = nums[pointer]
                    nums[pointer] = -999
                    duplicatesFound = 0
                    currentNumber = currentNumber + 1
                elif duplicatesFound == 0:
                    nums[currentNumber+1] = nums[pointer]
                    currentNumber = currentNumber + 1
            pointer = pointer + 1
        return currentNumber+1