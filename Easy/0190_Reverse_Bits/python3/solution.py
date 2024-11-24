class Solution:
    def reverseBits(self, n: int) -> int:
        bitsRemaining = 32
        result = 0
        while n > 0:
            result = result << 1
            result = result | (n & 1)
            n = n >> 1
            bitsRemaining -= 1
        return result << bitsRemaining
