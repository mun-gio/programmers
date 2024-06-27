def solution(s):
    parentheses = []
    for i in s:
        if i =="(":
            parentheses.append(i)
        elif len(parentheses) > 0:
            parentheses.pop()
        else: return False
    if len(parentheses) == 0:
        return True
    else:
        return False
