def solution(n):
    if n/7 <= 1:
        answer = 1
    elif n/7 <= int(n/7):
        answer = int(n/7)
    else:
        answer = int(n/7+1)
    return answer