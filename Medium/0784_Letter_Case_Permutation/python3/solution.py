class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        strings = set()
        self._letterCasePermutation(list(s), 0, strings)
        return list(strings)

    def _letterCasePermutation(self, s: List[str], start: int, strings: Set[str]):
        for index in range(start, len(s)):
            character = s[index]
            self._letterCasePermutation(s, index+1, strings)
            strings.add(''.join(s))
            if character.islower():
                s[index] = chr(ord(character)-32)
                strings.add(''.join(s))
                self._letterCasePermutation(s, index+1, strings)
            elif character.isupper():
                s[index] = chr(ord(character)+32)
                strings.add(''.join(s))
                self._letterCasePermutation(s, index+1, strings)
