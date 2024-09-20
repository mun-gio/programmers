def solution(myString):
    return sorted([part for part in myString.split('x') if part])