class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [1] * (n+1)
        ans[0] = 0
        latest = 0
        for i in range(1, n+1):
            if (i & (i - 1)) == 0:
                latest = i
            else:
                lookup = i ^ latest
                ans[i] = ans[lookup] + 1
        return ans
