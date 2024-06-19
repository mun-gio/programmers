def solution(arr1, arr2):
    answer = 0
    n = 0
    m = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        for i in range(len(arr1)):
            n += arr1[i]
            m += arr2[i]
        if n > m :
            answer = 1
        elif n < m :
            answer = -1
    return answer