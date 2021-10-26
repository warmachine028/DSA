# CODE 8c: Optimization of allConstruct using tabulation
from typing import Optional


def all_construct(target: str, word_bank: list[str]) -> list[Optional[list[str]]]:
    table = [[[]]] + [[] for _ in enumerate(target)]
    for current, _ in enumerate(target):
        if not table[current]: continue
        for word in word_bank:
            _next = current + len(word)
            if target[current: _next].startswith(word):
                current_ways = table[current]
                table[_next] += [*map(lambda way: [word] + way, current_ways)]
    
    return table[len(target)]


print(all_construct("", ['purp', 'p', 'ur', 'le', 'purpl']))
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
