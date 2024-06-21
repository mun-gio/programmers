def solution(n):
    answer = 0
    for i in range(len(str(n+1))):
        answer += (n//(10**i))-(n//(10**(i+1)))*10
    return answer