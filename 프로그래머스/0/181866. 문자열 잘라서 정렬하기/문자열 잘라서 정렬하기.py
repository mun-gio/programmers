def solution(myString):
    answer = sorted([part for part in myString.split('x') if part])
    return answer