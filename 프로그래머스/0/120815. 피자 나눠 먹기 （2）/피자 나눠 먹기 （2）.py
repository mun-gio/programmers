def solution(n):
    for i in range(n):
        if (6*(i+1))%n == 0:
            return i+1