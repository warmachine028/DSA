# CODE 6b: Optimization of CanConstruct using memoization


def can_construct(target: str, word_bank: list[str], memo=None) -> bool:
    if memo is None:
        memo = {}
    if target == '':
        return True
    if target in memo:
        return memo[target]
    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False


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
