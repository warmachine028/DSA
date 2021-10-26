# CODE 6a: Write a function canConstruct(target, wordBank) that accepts a target and an array of strings.
# It must return a boolean indicating whether or not the target can be constructed by concatenating
# elements of the wordBank array.
# You may reuse elements of wordBank as many times as needed.


def can_construct(target: str, word_bank: list[str]) -> bool:
    if target == '':
        return True
    for word in word_bank:
        if target.startswith(word):
            suffix = target.removeprefix(word)
            if can_construct(suffix, word_bank):
                return True
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
