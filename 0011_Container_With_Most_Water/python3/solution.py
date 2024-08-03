class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Greedy Choice Property: Curret Max Area
        Method 1: Greedy + Two Pointers: O(n), O(1)
            1. Start from the outside and work inward
            2. Choose a new side (update the lower) if it yields a new max area
        """
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            x = right - left
            area = x * min(height[left], height[right])
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area