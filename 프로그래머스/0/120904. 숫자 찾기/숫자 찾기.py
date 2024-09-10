def solution(num, k):
    n = len(str(num))
    for i in range(n):
        if str(num)[i] == str(k):
            return i+1
    return -1