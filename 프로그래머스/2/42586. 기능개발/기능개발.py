import math
def solution(progresses, speeds):
    p = len(progresses)
    remain = []
    li =[]
    j = 0
    for i in range(p):
        if (100 - progresses[i])/speeds[i] > (100 - progresses[i])//speeds[i]:
            num = (100 - progresses[i])//speeds[i] + 1
        else:
            num = (100 - progresses[i])//speeds[i]
        remain.append(num)
    for i in range(p):
        if i == 0 or remain[i] > remain[j]:
            li.append(1)
            j = i
        elif remain[i] <= remain[j]:
            li[-1] += 1
    return li