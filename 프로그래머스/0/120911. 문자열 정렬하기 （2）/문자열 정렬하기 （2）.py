def solution(my_string):
    answer = sorted(my_string.lower())
    S = ''
    for s in answer:
        S += s
    return S