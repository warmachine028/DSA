# CODE 16: Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
# Check whether A has redundant braces or not. Return 1 if A has redundant braces, else return 0.
# Partially Correct

def braces(string: str) -> int:
    stack = []
    
    for item in string:
        if not item.isalnum():
            if item == ')':
                if not stack[-1].isalnum() and len(stack) >= 2:
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(')')
            else:
                stack.append(item)
    if not stack:
        return 0
    if stack[-1] != ')':
        return 0
    return 1


print(braces("((a + b))"))  # 1
print(braces("(a + (a + b))"))  # 0
print(braces("(a + b)"))  # 0
print(braces("(a+b)*((b+c)/d))"))  # 1
