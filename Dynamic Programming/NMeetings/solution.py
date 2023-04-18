import sys
class Solution:
    @staticmethod
    def main(args: list[str]) -> None:
        starts = [*map(int, input().split())]
        ends = [*map(int, input().split())]
        meetings = [meet for meet in zip(starts, ends)]

        meetings.sort(key=lambda time: (time[1], time[0]))
        first = 0
        second = count = 1
        while second < len(meetings):
            if meetings[first][1] >= meetings[second][0]:
                second += 1
                continue
            first = second
            second += 1
            count += 1
        print(count)


"""
I/P
-> 1 3 0 5 8 5
-> 2 4 6 7 9 9
O/P
-> 4
"""
