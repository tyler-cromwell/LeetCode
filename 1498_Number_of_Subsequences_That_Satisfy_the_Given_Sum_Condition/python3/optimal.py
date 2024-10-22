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

        # 2.5) Precompute powers to save time O(n), O(n)
        powers = [1] * n
        for i in range(1, n):
            powers[i] = powers[i - 1] * 2 % mod

        # 3) Move inward O(n), O(1)
        while left <= right:
            if (nums[left] + nums[right]) <= target:
                # Accumulate number of new subsequences to include
                result += powers[right-left]
                left += 1
            else:
                right -= 1

        return result % mod
