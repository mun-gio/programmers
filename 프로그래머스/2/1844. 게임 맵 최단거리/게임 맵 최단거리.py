from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    
    if maps[0][0] == 1:
        q.append((0,0,1))
        visited[0][0] = True
    while q:
        r, c, dist = q.popleft()
        if r == n-1 and c == m-1:
            return dist
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[r][c] == 1:
                if not visited[nr][nc]:
                    q.append((nr, nc, dist+1))
                    visited[nr][nc] = True
    return -1