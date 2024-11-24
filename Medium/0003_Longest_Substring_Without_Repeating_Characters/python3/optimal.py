class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Method 1: Sliding Window + Hashing: O(n), O(n)
        """
        seen = {}
        left = 0
        length = 0
        for index in range(len(s)):
            character = s[index]
            if character in seen and seen[character] >= left:
                left = seen[character]+1
            seen[character] = index
            length = max(length, index+1-left)
        return length