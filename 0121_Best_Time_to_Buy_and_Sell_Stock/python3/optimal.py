from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Method 1: Dynamic Programming (Two-Pointers-style): O(n), O(1)
        """
        days = len(prices)
        minday = 0
        minprice = prices[minday]
        maxprofit = 0
        for day in range(1, days):
            if prices[day] < minprice:
                minprice = prices[day]
                minday = day
            else:
                profit = prices[day] - minprice
                if profit > maxprofit:
                    maxprofit = profit

        return maxprofit
