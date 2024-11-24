class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        first = 0
        second = 0
        while first < n:
            if not s[first].isspace():
                second = first
                while second < n and not s[second].isspace():
                    second += 1
                words.append(s[first:second])
                first = second
            else:
                first += 1

        words.reverse()
        return ' '.join(words)
