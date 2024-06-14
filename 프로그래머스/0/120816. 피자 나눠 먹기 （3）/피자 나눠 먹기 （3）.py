def solution(slice, n):
    if n % slice == 0:
        answer = n/slice
    elif  n/slice <= int(n/slice):
        answer = int(n/slice)
    else:
        answer = int(n/slice+1)
    return answer