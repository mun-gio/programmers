def solution(participant, completion):
    completed = {}
    p_list = {}
    for player in participant:
        if player not in p_list:
            p_list[player] = 1
        else:
            p_list[player] += 1
    for player in completion:
        if player not in completed:
            completed[player] = 1
        else:
            completed[player] += 1
    for key, value in p_list.items():
        if key not in completed or value != completed[key]:
            return key
        
            