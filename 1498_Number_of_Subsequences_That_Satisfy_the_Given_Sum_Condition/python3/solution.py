class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # 1) Sort the input - O(nlog(n)), O(n)
        nums.sort()

        # 2) Initialize pointers
        n = len(nums)
        mod = ((10**9)+7)
        result = 0
        left = 0
        right = n-1

        # 3) Move inward
        while left <= right:
            v1 = nums[left]
            v2 = nums[right]

            if (v1+v2) <= target:
                # Accumulate number of new subsequences to include
                result += pow(2, right-left)
                left += 1
            else:
                right -= 1

        return result % mod
