def solution(num_list):
    answer = []
    n1 = 0
    n2 = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            n1 += 1
        else:
            n2 += 1
    answer.append(n1)
    answer.append(n2)
    return answer