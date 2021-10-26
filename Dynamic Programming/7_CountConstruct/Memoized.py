# CODE 7b: Optimization of countConstruct using memoization

def count_construct(target: str, word_bank: list[str], memo=None) -> int:
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    
    if target == '':
        return 1
    
    total_ways = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)  # target[len(word):]
            num_ways = count_construct(suffix, word_bank, memo)
            total_ways += num_ways
    
    memo[target] = total_ways
    return total_ways


print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e',
                                                                   'ee',
                                                                   'eee',
                                                                   'eeee',
                                                                   'eeeee',
                                                                   'eeeeee']))  # 0
