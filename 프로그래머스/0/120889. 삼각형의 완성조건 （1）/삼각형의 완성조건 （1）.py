def solution(sides):
    answer = 0
    n = 0
    sum = 0
    for i in range(len(sides)):
        if n < sides[i]:
            sum += n
            n = sides[i]
        else:
            sum += sides[i]
    if n < sum:
        answer = 1
    else:
        answer = 2
    return answer