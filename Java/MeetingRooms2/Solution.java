package MeetingRooms2;

import java.util.List;
//import java.util.stream.Collectors;

import MeetingRooms.Interval;


public class Solution {
    /**
     * @param intervals: an array of meeting time intervals
     * @return: the minimum number of conference rooms required
     */
    public int minMeetingRooms(List<Interval> intervals) {
        List<Integer> starts = intervals.stream().map(interval -> interval.start).sorted().toList(),
                ends = intervals.stream().map(interval -> interval.end).sorted().toList();
//        List <Integer> starts = intervals.stream().map(interval -> interval.start).sorted().collect(Collectors.toList()),
//                       ends =   intervals.stream().map(interval -> interval.end).sorted().collect(Collectors.toList());

        int result, meeting_rooms;
        int start, end;
        result = meeting_rooms = start = end = 0;

        while (start < intervals.size()) {
            if (starts.get(start) < ends.get(end)) {
                start++;
                meeting_rooms++;
            } else {
                end++;
                meeting_rooms--;
            }
            result = Math.max(result, meeting_rooms);
        }
        return result;
    }
}