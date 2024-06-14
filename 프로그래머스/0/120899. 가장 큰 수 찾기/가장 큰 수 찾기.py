def solution(array):
    answer = []
    m = 0
    for i in range(len(array)):
        if array[i] > m:
            m = array[i]
    answer.append(m)
    for i in range(len(array)):
        if array[i] == m:
            answer.append(i)
    return answer