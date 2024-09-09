def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
        elif i == len(arr)-1:
            return -1