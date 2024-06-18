def solution(num_list):
    a_1 = ''
    a_2 = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            a_1 += str(num_list[i])
        else:
            a_2 += str(num_list[i])
    return int(a_2) + int(a_1)