from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for perm in permutations(dungeons):
        current_fatigue = k
        count = 0
        
        for dungeon in perm:
            min_fatigue, used_fatigue = dungeon
            if current_fatigue >= min_fatigue:
                current_fatigue -= used_fatigue
                count += 1
            else:
                break
        
        max_count = max(max_count, count)
    
    return max_count
