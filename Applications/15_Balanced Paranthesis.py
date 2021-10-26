# CODE 15: Given a string A consisting only of '(' and ')'.
# You need to find whether parentheses in A is balanced or not ,if it is balanced then return 1 else return 0.

def balanced(string: str) -> int:
    stack = []
    for item in string:
        if item == ')':
            if not stack:
                return 0
            stack.pop()
        else:
            stack.append(item)
    return int(not stack)


print(balanced('()'))  # 1
print(balanced('('))  # 0
print(balanced(')'))  # 0
print(balanced('()('))  # 0
print(balanced('(('))  # 0
print(balanced('(())))()'))  # 0
print(balanced('()()'))  # 1
print(balanced('())'))  # 0
print(balanced('))))'))  # 0
print(balanced('())'))  # 0
