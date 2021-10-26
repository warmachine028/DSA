# CODE 8a: Write a function allConstruct(target, wordBank) that accepts a target and an array of strings.
# It must return a 2D array containing all the ways that the target can be constructed by concatenating
# elements of the wordBank array

# You may reuse elements of wordBank as many times as needed.

def all_construct(target, word_bank):
    if target == '':
        return [[]]
    
    total_ways = []
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target.removeprefix(word)
            suffix_ways = all_construct(suffix, word_bank)
            total_ways += [*map(lambda way: [word] + way, suffix_ways)]
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
