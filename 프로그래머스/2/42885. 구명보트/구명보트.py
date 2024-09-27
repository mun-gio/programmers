def solution(people, limit):
    people.sort(reverse = True)
    answer = 0
    i = 0
    j = len(people) -1
    
    while True:
        if i == j:
            answer += 1
            return answer
        elif i > j:
            return answer
        elif people[i] + people[j] <= limit:
            i += 1
            j -= 1
            answer += 1
        else:
            i += 1
            answer += 1
        