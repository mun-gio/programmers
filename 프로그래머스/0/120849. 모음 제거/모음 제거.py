def solution(my_string):
    answer = ''
    s = 'aeiou'
    for i in my_string:
        if i not in s:
            answer += i
    return answer