# CODE 7a: Write a function countConstruct(target, wordBank) that accepts a target and an array of strings.
# It must return the number of ways that the target can be constructed by concatenating the
# elements of the wordBank array.
# You may reuse elements of wordBank as many times as needed.


def count_construct(target: str, word_bank: list[str]) -> int:
    if target == '':
        return 1
    total_ways = 0
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target.removeprefix(word)  # target[len(word):]
            num_ways = count_construct(suffix, word_bank)
            total_ways += num_ways
    return total_ways


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
