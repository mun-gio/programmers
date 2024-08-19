def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(cur_v):
        visited[cur_v] = True
        for next_v in range(n):
            # 연결이 안된거니까 skip
            if computers[cur_v][next_v] == 0: continue
            if not visited[next_v]:
                dfs(next_v)
                
    for cur_v in range(n):
        if not visited[cur_v]:
            dfs(cur_v)
            answer += 1
    return answer