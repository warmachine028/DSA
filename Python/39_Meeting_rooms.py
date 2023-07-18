"""
CODE 39: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict


Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            curr_meet = intervals[i]
            last_meet = intervals[i - 1]

            if last_meet.end > curr_meet.start:
                return False

        return True


class Main:
    @staticmethod
    def main():
        solution = Solution()

        # Test Case 1
        intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        result1 = solution.can_attend_meetings(intervals1)
        print("Output for Test Case 1:", result1)

        # Test Case 2
        intervals2 = [Interval(5, 8), Interval(9, 15)]
        result2 = solution.can_attend_meetings(intervals2)
        print("Output for Test Case 2:", result2)

        # Test Case 3
        intervals3 = [
            Interval(465, 497),
            Interval(386, 462),
            Interval(354, 380),
            Interval(134, 189),
            Interval(199, 282),
            Interval(18, 104),
            Interval(499, 562),
            Interval(4, 14),
            Interval(111, 129),
            Interval(292, 345),
        ]
        result3 = solution.can_attend_meetings(intervals3)
        print("Output for Test Case 3:", result3)


if __name__ == "__main__": 
    # Run the main function
    Main.main()
