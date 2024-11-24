class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # O(n^2): Brute force
        
        n = len(nums)
            
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
        return []
        """
        
        # O(n): Complement hash look up.
        
        n = len(nums)
        D = dict(zip(nums, range(n)))
        
        for i in range(n):
            complement = target - nums[i]
            if complement in D and i != D[complement]:
                return [i, D[complement]]
            
        return []
