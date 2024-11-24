class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            if n & 1 == 1:
                weight += 1
            n = n >> 1
        return weight
