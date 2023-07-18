package MeetingRooms;

import java.util.*;

public class Solution {

    public static void print(List<Interval> intervals) {
        for (Interval interval : intervals)
            System.out.println(interval.start + " " + interval.end);
        System.out.println();
    }

    /**
     * @param intervals: an array of meeting time intervals
     * @return: if a person could attend all meetings
     */
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort(Comparator.comparingInt(interval -> interval.start));

        for (int i = 1; i < intervals.size(); i++) {
            Interval last_meet = intervals.get(i - 1),
                    curr_meet = intervals.get(i);
            if (last_meet.end > curr_meet.start)
                return false;
        }
        return true;
    }
}