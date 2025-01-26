from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)

        heaviest = -heappop(stones)
        while len(stones) > 0:
            second = -heappop(stones)
            if heaviest != second:
                diff = heaviest-second
                heappush(stones, -diff)
            elif len(stones) == 0:
                return 0
            heaviest = -heappop(stones)

        return heaviest