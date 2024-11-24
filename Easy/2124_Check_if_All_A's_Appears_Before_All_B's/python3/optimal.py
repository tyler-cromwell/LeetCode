class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == 'b' and s[j] == 'a':
                return False
            elif s[i] == 'a' and s[j] == 'b':
                i += 1
                j -= 1
            elif s[i] == 'a' and s[j] == 'a':
                i += 1
            else:
                j -= 1
        return True
