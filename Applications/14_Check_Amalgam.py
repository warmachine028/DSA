# CODE 14: Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
from collections import Counter


def is_anagram(string1: str, string2: str) -> bool:
    window = len(string1)
    hash_map1 = Counter(string1)
    for i in range(len(string2) - window + 1):
        hash_map2 = Counter(string2[i:i + window])
        if hash_map2 == hash_map1:
            return True
    return False


print(is_anagram("ab", "eidbaooo"))
print(is_anagram("ab", "eidboaoo"))
