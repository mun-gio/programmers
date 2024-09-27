def solution(s):
    stack =[]
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
        else:
            return False
    if not stack:
        return True
    else:
        return False