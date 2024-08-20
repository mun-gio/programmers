from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    q.append([-numbers[0], 0])
    q.append([+numbers[0], 0])
    while q:
        num, i = q.popleft()
        i += 1
        if i < n:
            q.append([num + numbers[i], i])
            q.append([num - numbers[i], i])
        else:
            if num == target:
                answer += 1
    return answer