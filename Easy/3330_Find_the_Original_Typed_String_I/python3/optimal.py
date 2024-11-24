class Solution:
    def possibleStringCount(self, word: str) -> int:
        totalCount = 1
        ptrLeft = 0
        ptrRight = 1

        while ptrRight < len(word):
            if word[ptrLeft] == word[ptrRight]:
                totalCount += 1
                ptrRight += 1
            else:
                ptrLeft = ptrRight
                ptrRight += 1

        return totalCount
