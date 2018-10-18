# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda x: x.start)
        result = [intervals[0]]
        for num in intervals:
            if num.start <= result[-1].end: #if starts overlapping, merge ends (start already insenquence)
                result[-1].end = max(num.end, result[-1].end)
            else:
                result.append(num)
        return result

# Given a collection of intervals, merge all overlapping intervals.
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].