# CODE 6c: Optimization of CanConstruct using tabulation


def can_construct(target: str, word_bank: list[str]) -> bool:
    table = [True] + [False] * len(target)
    for current, _ in enumerate(target):
        if table[current] is False: continue
        for word in word_bank:
            _next = current + len(word)
            if target[current: _next].startswith(word):
                table[_next] = True
    
    return table[len(target)]


print(can_construct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct("skateboard", ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print(can_construct("enterapotentpot", ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # True
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
]))  # False
