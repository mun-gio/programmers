def solution(my_string, m, c):
    answer =''
    for s in range(c-1,len(my_string),m):
        answer += my_string[s]
    return answer