def solution(n):
    answer = 0
    i = n**(1/2)
    if i % 1 == 0 :
        answer = 1
    else:
        answer = 2
    return answer