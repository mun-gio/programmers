def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        
    n1n, n2n, n3n = 0,0,0
    answer = []
    
    if len(answers) > len(n1):
        for i in range(len(answers)-len(n1)):
            n1.append(n1[i])
    if len(answers) > len(n2):
        for i in range(len(answers)-len(n2)):
            n2.append(n2[i])
    if len(answers) > len(n3):
        for i in range(len(answers)-len(n3)):
            n3.append(n3[i])
    
    for i in range(len(answers)):
        if answers[i] == n1[i]:
            n1n += 1
        if answers[i] == n2[i]:
            n2n += 1
        if answers[i] == n3[i]:
            n3n += 1
            
    if n1n == max(n1n, n2n, n3n):
        answer.append(1)
    if n2n == max(n1n, n2n, n3n):
        answer.append(2)
    if n3n == max(n1n, n2n, n3n):
        answer.append(3)
    return answer