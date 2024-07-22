def solution(s):
    stack = []
    for p in s:
        if p =="(":
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack
