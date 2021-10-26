# CODE 8b: Optimization of allConstruct using memoization
from typing import Optional


def all_construct(target: str, word_bank: list[str], memo=None) -> list[Optional[list[str]]]:
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    if target == '':
        return [[]]
    
    total_ways = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            suffix_ways = all_construct(suffix, word_bank, memo)
            total_ways += [*map(lambda way: [word] + way, suffix_ways)]
    
    memo[target] = total_ways
    return total_ways


print(all_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
# [
#   [ purp, le ],
#   [ p, ur, p, le ]
# ]
print(all_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
# [
#   [ ab, cd, ef ],
#   [ ab, c, def ],
#   [ abc, def ],
#   [ abcd, ef ]
# ]
print(all_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
# [
# 	['enter', 'a', 'p', 'ot', 'ent', 'p', 'ot']
# 	['enter', 'a', 'p', 'ot', 'ent', 'p', 'o', 't']
# 	['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'ot']
# 	['enter', 'a', 'p', 'o', 't', 'ent', 'p', 'o', 't']
# ]
print(all_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
# []
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaz", [
    'a',
    'aa',
    'aaa',
    'aaaa',
    'aaaaa',
]))
# []
