# CODE 28: Given a string A representing a roman numeral.
#  Convert A into integer.
# A is guaranteed to be within the range from 1 to 3999.
# NOTE: Read more
# details about roman numerals at Roman Numeric System
#
#
# Input Format
# The only argument given is string A.
# Output Format
# Return an integer which is the integer version of roman numeral string.
# For Example
#
# Input 1:
#     A = "XIV"
# Output 1:
#     14
#
# Input 2:
#     A = "XX"
# Output 2:
#     20

def roman_to_integer(roman: str) -> int:
    maps = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(roman)):
        curr = roman[i]
        _nxt = roman[i + 1 if i + 1 < len(roman) else i]
        result += -maps[curr] if maps[curr] < maps[_nxt] else maps[curr]
    
    return result


print(roman_to_integer('I'))
print(roman_to_integer('IX'))
print(roman_to_integer('XI'))
print(roman_to_integer('II'))
print(roman_to_integer('IV'))
print(roman_to_integer('XX'))
print(roman_to_integer('XXI'))
print(roman_to_integer('MMMCMXCIX'))
