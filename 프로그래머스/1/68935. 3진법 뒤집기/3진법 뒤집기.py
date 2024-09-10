def solution(n):
    answer = 0
    mid =[]
    while n:
        mid.append(n%3)
        n = n//3
    mid.reverse()
    for i in range(len(mid)):
        answer += mid[i]*3**i
    return answer