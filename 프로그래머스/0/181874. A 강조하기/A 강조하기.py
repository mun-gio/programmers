def solution(myString):
    answer = ''
    for a in myString:
        if a == 'a' or a == "A":
            answer += a.upper()
        else:
            answer += a.lower()
    return answer