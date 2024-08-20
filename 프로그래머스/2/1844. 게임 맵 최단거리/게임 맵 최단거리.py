from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False] * m for _ in range(n)]
    
    def dfs(r, c):
        # 초기 설정
        q = deque()
        # 시작점 예약
        q.append((r,c))
        visited[r][c] = True
        while q:
            # 현재 노드 방문
            cur_r, cur_c = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_r + dc[i]
                if 0 <= next_r < n and 0 <= next_c < m and maps[next_r][next_c] == 1:
                    dfs(r, c)
    for r in range(n):
        for c in range(m):
            if maps[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                answer += 1
    return answer