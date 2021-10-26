# CODE 13: Find the powerSet of a given string

def power_set(string: str) -> list[str]:  # Time Complexity: 2^n
    n = len(string)
    p_set = []
    for i in range(1 << n):  # 2^n
        subset = ''.join(string[j] for j in range(n) if i & 1 << j)
        p_set.append(subset)
    # Optional: Sorting the string length wise for better visualizing
    p_set.sort(key=len)
    return p_set


# The One Liner approach
# power_set = lambda s:sorted((''.join(s[j] for j in range(len(s)) if i & 1 << j) for i in range(1 << len(s))), key=len)

print(power_set('abc'))  # ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
print(power_set('abcd'))  # ['', 'a', 'b', 'c', ..., 'acd', 'bcd', 'abcd']
print(power_set('abcde'))  # ['', 'a', 'b', 'c', ..., 'acde', 'bcde', 'abcde']
print(power_set('abcdef'))  # ['', 'a', 'b', 'c', ..., 'acdef', 'bcdef', 'abcdef']
print(power_set('abcdefg'))  # ['', 'a', 'b', 'c', ...,'acdefg', 'bcdefg', 'abcdefg']

# TIP: A string always has a superset of length 2^n, where n is the length of the string
