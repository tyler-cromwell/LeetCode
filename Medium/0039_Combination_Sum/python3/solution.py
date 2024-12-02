#!/usr/bin/env python3

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        tempSolution = []
        n = len(candidates)
        self._combinationSum(candidates, target, 0, 0, n, tempSolution, solutions)
        return solutions

    def _combinationSum(self, candidates: List[int], target: int, total: int, index: int, length: int, tempSolution: List[int], solutions: List[List[int]]):
        if index >= length:
            # We've run out of options
            return
        elif total == target:
            # Just right
            solutions.append(tempSolution[:])
            return
        elif total < target:
            # Sum hasn't reached the target, keep trying
            candidate = candidates[index]
            if candidate <= target:
                # Choose the current number
                tempSolution.append(candidate)
                self._combinationSum(candidates, target, total+candidate, index, length, tempSolution, solutions)
                tempSolution.pop(-1)

            # Do NOT choose the current number
            self._combinationSum(candidates, target, total, index+1, length, tempSolution, solutions)
            return
