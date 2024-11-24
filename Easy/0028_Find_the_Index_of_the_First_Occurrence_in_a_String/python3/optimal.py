class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        base = 0
        while base < (n-m+1):
            count = 0
            if haystack[base] == needle[0]:
                for i in range(m):
                    if haystack[base+i] != needle[i]:
                        break
                    else:
                        count += 1
                if count == m:
                    return base
            base += 1
        return -1
