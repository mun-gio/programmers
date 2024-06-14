def solution(age):
    answer = ''
    a = 'abcdefghij'
    for i in str(age):
        answer += a[int(i)]
    return answer