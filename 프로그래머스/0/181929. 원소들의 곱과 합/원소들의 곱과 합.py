def solution(num_list):
    answer = 0
    s = 0
    x = 1
    for i in num_list:
        x *= i
    for i in num_list:
        s += i
    if x < s*s:
        answer = 1
    return answer