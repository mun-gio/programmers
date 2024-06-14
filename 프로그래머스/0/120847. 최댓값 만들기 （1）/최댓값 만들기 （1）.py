def solution(numbers):
    answer = 0
    a = 0
    for i in range(len(numbers)):
        if numbers[i] > answer:
            a = answer
            answer = numbers[i]
        elif numbers[i] > a:
            a = numbers[i]
            
    return answer * a