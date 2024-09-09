from collections import deque
def solution(priorities, location):
    q = deque([i,p] for i,p in enumerate(priorities))
    answer = 0
    
    while True:
        cur = q.popleft()
        if any(cur[1] < i[1] for i in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer