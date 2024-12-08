from heapq import *

class MedianFinder:
    def __init__(self):
        self._minheap = []
        self._maxheap = []
        self._minsize = 0
        self._maxsize = 0

    def addNum(self, num: int) -> None:
        heappush(self._maxheap, -1*num)
        self._maxsize += 1
        if (self._maxheap and self._minheap and (-1 * self._maxheap[0]) > self._minheap[0]):
            # Top of Max-Heap is greater than "top" of Min-Heap, move it over
            val = -1 * heappop(self._maxheap)
            self._maxsize -= 1
            heappush(self._minheap, val)
            self._minsize += 1

        if self._minsize > (self._maxsize + 1):
            value = heappop(self._minheap)
            self._minsize -= 1
            heappush(self._maxheap, -1*value)
            self._maxsize += 1
        elif self._maxsize > (self._minsize + 1):
            value = -1*heappop(self._maxheap)
            self._maxsize -= 1
            heappush(self._minheap, value)
            self._minsize += 1

            
    def findMedian(self) -> float:
        if self._minsize == 0 and self._maxsize == 0:
            return 0
        elif self._minsize == 0:
            return -1*self._maxheap[0]
        elif self._maxsize == 0:
            return self._minheap[0]

        if self._minsize > self._maxsize:
            return self._minheap[0]
        elif self._maxsize > self._minsize:
            return -1*self._maxheap[0]
        else:
            return (self._minheap[0] + -1*self._maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
