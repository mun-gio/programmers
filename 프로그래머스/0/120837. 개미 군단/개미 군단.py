def solution(hp):
    a1 = int(hp/5)
    a2 = int((hp%5)/3)
    a3 = int(((hp%5)%3)/1)
    answer = a1+a2+a3
    return answer