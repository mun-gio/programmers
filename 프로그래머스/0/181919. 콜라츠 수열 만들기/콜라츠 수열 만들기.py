def solution(n):
    answer = []
    answer.append(n)
    while True:
        if answer[-1] % 2 == 0:
            answer.append(answer[-1]/2)
        elif answer[-1] == 1:
            return answer
        else:
            answer.append(answer[-1]*3+1)