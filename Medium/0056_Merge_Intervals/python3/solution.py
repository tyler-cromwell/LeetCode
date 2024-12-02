#!/usr/bin/env python3

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge(array1: List[int], array2: List[int]) -> List[int]:
            start1 = array1[0]
            start2 = array2[0]
            end1 = array1[1]
            end2 = array2[1]

            if end1 >= end2:
                # Merge (full-overlap)
                return [start1, end1]
            elif end1 >= start2:
                # Merge (partial-overlap)
                return [start1, end2]
            else:
                # No merge (no overlap)
                return []

        # Sort the input by start member
        sortedIntervals = sorted(intervals, key=lambda m: m[0])

        # Iterate forward, merging intervals
        n = len(sortedIntervals)
        result = [sortedIntervals[0]]
        r = 0
        i = 1

        while i < n:
            array1 = result[r]
            array2 = sortedIntervals[i]

            merged = merge(array1, array2)
            if merged == []:
                # Cannot merge, include just the next, advance both
                result.append(array2)
                r += 1
            else:
                # Merged, updated lastest merged, advance input
                result[-1] = merged
            i += 1

        return result
