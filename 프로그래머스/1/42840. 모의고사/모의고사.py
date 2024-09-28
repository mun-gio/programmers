def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        
    score = [0,0,0]
    answer = []
    
    for idx, num in enumerate(answers):
        if num == n1[idx%len(n1)]:
            score[0] += 1
        if num == n2[idx%len(n2)]:
            score[1] += 1
        if num == n3[idx%len(n3)]:
            score[2] += 1
            
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer