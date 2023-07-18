"""
CODE 40: Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

from typing import List

"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        result = meeting_rooms = 0
        start = end = 0

        while start < len(intervals):
            if starts[start] < ends[end]:
                start += 1
                meeting_rooms += 1
            else:
                end += 1
                meeting_rooms -= 1
            result = max(result, meeting_rooms)
        return result
