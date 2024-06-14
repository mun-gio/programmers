def solution(my_string):
    answer = []
    n = '1234567890'
    for i in my_string:
        if i in n:
            answer.append(int(i))
    answer.sort()
    return answer