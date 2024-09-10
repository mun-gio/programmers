from collections import deque
def solution(sizes):
    sizes.sort(reverse=True)
    q = deque(i for i in sizes)
    mi, mj = q.popleft()
    
    while q:
        i, j = q.popleft()
        if mj < j:
            if mi >= j and mj >= i:
                continue
            elif mi < j:
                if mj < i:
                    mj = i
                    mi = j
                elif mj >= i:
                    mi = j
            elif mj < i:
                if i > j:
                    mj = j
                else:
                    mj = i
            
    return mi * mj
        
        