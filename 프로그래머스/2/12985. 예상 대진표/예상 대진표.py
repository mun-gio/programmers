def solution(n,a,b):
    answer = 0
    for i in range(n):
        if a == b:
            return answer
        else:
            a = (a+1)//2
            b = (b+1)//2
            answer += 1