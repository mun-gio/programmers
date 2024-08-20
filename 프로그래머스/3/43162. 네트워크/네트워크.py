from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    queue = deque()
    
    def bfs(cur_v):
        queue.append(cur_v)
        visited[cur_v] = True
        while queue:
            cur_v = queue.popleft()
            for next_v in range(n):
                if computers[cur_v][next_v] == 1 and not visited[next_v]:
                    queue.append(next_v)
                    visited[next_v] = True
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)
    return answer