package MeetingRooms2;

import MeetingRooms.Interval;

import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test Case 1
        List<Interval> intervals1 = Arrays.asList(
                new Interval(0, 30),
                new Interval(5, 10),
                new Interval(15, 20));
        int result1 = solution.minMeetingRooms(intervals1);
        System.out.println("Output for Test Case 1: " + result1);

        // Test Case 2
        List<Interval> intervals2 = Arrays.asList(
                new Interval(5, 8),
                new Interval(9, 15));
        int result2 = solution.minMeetingRooms(intervals2);
        System.out.println("Output for Test Case 2: " + result2);

        // Test Case 3
        List<Interval> intervals3 = Arrays.asList(
                new Interval(465, 497),
                new Interval(386, 462),
                new Interval(354, 380),
                new Interval(134, 189),
                new Interval(199, 282),
                new Interval(18, 104),
                new Interval(499, 562),
                new Interval(4, 14),
                new Interval(111, 129),
                new Interval(292, 345));
        int result3 = solution.minMeetingRooms(intervals3);
        System.out.println("Output for Test Case 3: " + result3);
    }
}
