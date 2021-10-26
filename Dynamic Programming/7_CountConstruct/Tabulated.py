# CODE 7c: Optimization of countConstruct using tabulation

def count_construct(target: str, word_bank: list[str]) -> int:
    table = [1] + [0] * len(target)
    
    for current, _ in enumerate(target):
        if table[current] == 0: continue
        for word in word_bank:
            _next = current + len(word)
            if target[current:_next].startswith(word):
                table[_next] += table[current]
    
    return table[len(target)]


print(count_construct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
]))  # 0
