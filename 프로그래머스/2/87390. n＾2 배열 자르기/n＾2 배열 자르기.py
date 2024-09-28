def solution(n, left, right):
    a = []
    for i in range(left, right+1):
        a.append(max(i//n, i%n)+1)
    return a