def solution(s):
    left_parentheses = 0
    right_parentheses = 0
    for i in s:
        if i == "(":
            left_parentheses +=1
        elif i == ")":
            right_parentheses +=1
            if left_parentheses < right_parentheses:
                return False
            
    if right_parentheses == left_parentheses:
        return True
    else:
        return False
