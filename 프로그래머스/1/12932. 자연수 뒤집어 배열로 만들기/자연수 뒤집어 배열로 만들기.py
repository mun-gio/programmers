def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append((n//(10**i))-(n//10**(i+1))*10)
    return answer