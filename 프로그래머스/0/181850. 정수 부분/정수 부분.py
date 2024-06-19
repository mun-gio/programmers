def solution(flo):
    answer = 0
    if flo < int(flo):
        answer = int(flo) - 1
    else:
        answer = int(flo)
    return answer