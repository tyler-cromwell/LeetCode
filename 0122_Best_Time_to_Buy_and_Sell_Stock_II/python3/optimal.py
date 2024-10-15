class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index-1]:
                maxprofit = max(maxprofit, maxprofit + prices[index] - prices[index-1])
        return maxprofit
