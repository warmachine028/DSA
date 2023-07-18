package MeetingRooms;

/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
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
*/
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
		boolean result1 = solution.canAttendMeetings(intervals1);
		System.out.println("Output for Test Case 1: " + result1);

		// Test Case 2
		List<Interval> intervals2 = Arrays.asList(
				new Interval(5, 8),
				new Interval(9, 15));
		boolean result2 = solution.canAttendMeetings(intervals2);
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
		boolean result3 = solution.canAttendMeetings(intervals3);
		System.out.println("Output for Test Case 3: " + result3);
	}
}

// $> cd ..; javac .\MeetingRooms\*.java; java MeetingRooms.Main; del
// .\MeetingRooms\*.class
