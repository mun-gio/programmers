def solution(myString):
    answer = []
    n = 0
    for s in myString:
        if s == 'x':
            answer.append(n)
            n = 0
        else:
            n += 1
    answer.append(n)
    return answer
            