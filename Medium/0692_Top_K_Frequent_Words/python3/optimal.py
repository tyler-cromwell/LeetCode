import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequencies of each string
        d = {}
        for word in words:
            if word not in d: d[word] = 1
            else: d[word] = d[word] + 1

        # Heapify
        maxheap = []
        for key,value in d.items(): heapq.heappush(maxheap, (-1*value, key))

        # Prepare result
        result = []
        for i in range(k): result.append(heapq.heappop(maxheap)[1])
        return result
