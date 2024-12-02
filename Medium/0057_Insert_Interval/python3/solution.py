#!/usr/bin/env python3

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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

        # Find start point
        n = len(intervals)
        i = 0
        while i < n:
            if newInterval[0] <= intervals[i][0]:
                break
            i += 1

        # Insert the new interval
        if i == n and n == 0:
            return [newInterval]
        elif i == n:
            # start would be -1
            # append to end and return
            array1 = intervals[i-1]
            array2 = newInterval
            merged = merge(array1, array2)
            if merged == []:
                intervals.append(newInterval)
            else:
                intervals[i-1] = merged
            return intervals

        intervals.insert(i, newInterval)
        n += 1

        # Cascade (start == i)
        if i >= 1:
            # Check backwards
            array1 = intervals[i-1]
            array2 = intervals[i+0]

            merged = merge(array1, array2)
            if merged != []:
                # Merged, updated lastest merged, advance input
                intervals[i] = merged
                intervals.pop(i-1)
                n -= 1
                i -= 1

        r = 0

        while i < (n-1):
            array1 = intervals[i+0]
            array2 = intervals[i+1]

            merged = merge(array1, array2)
            if merged == []:
                # Cannot merge, stop the cascade
                break
            else:
                # Merged, updated lastest merged, advance input
                intervals[i] = merged
                intervals.pop(i+1)
                n -= 1

        return intervals
