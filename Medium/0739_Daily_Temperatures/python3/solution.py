class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answers = [0] * n

        for i in range(n):
            t1 = temperatures[i]
            while stack and t1 > stack[-1][0]:
                t2, j = stack.pop(-1)
                answers[j] = i-j
            stack.append((t1, i))

        return answers
