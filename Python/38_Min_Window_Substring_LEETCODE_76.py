"""
CODE 38: Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".


Eg 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


Eg 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Eg 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

"""

from collections import Counter

class Solution:
    @staticmethod
    def minWindowSubstring(s: str, t:str) -> str:
        result = ""
        map1, map2 = Counter(t), Counter()
        count, curCount = len(t), 0
        i = j = -1
        while True:
            flag1 = flag2 = False
            while i < len(s) - 1 and curCount < count:
                # Including character
                i += 1
                character = s[i]
                map2[character] += 1

                # increment curCount if essential character included
                if map2[character] <= map1[character]:
                    curCount += 1
                flag1 = True
            
            while j < i and curCount == count:
                # comparing with sub string
                subString = s[j + 1 : i + 1]
                if not result or len(subString) < len(result):
                    result = subString

                # Excluding character
                j += 1
                character = s[j]
                map2[character] -= 1 if map2[character] else 0

                # decrement curCount if essesntial character excluded
                if map2[character] < map1[character]:
                    curCount -= 1
                flag2 = True


            if not all((flag1, flag2)):
                break
        return result
    

if __name__ == "__main__": 
    assert Solution.minWindowSubstring(s = "ADOBECODEBANC", t = "ABC") == "BANC", "Wrong Output"
    assert Solution.minWindowSubstring(s = "a", t = "a") == "a", "Wrong Output"
    assert Solution.minWindowSubstring(s = "a", t = "aa") == "", "Wrong Output"

