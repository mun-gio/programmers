def solution(num_list):
    n = len(num_list)
    n1 = 0
    n2 = 0
    for i in range(n):
        if i % 2 == 0:
            n1 += num_list[i]
        else:
            n2 += num_list[i]
    if n1 > n2:
        return n1
    else:
        return n2