class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while target > 1:
            if maxDoubles > 0 and target % 2 == 0:
                target /= 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                return steps + int(target) - 1
            else:
                target -= 1
            steps += 1
        return steps
