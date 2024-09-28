def solution(s):
    stack = []
    s = s.replace('{','')
    s = s.replace('}','')
    s = s.split(',')
    
    s_dict = {}
    for idx, num in enumerate(s):
        num = int(num)
        if num not in s_dict:
            s_dict[num] = 1
        else:
            s_dict[num] += 1
    answer = []
    for i in range(len(s_dict)):
        answer.append(max(s_dict, key = s_dict.get))
        s_dict.pop(max(s_dict, key = s_dict.get))
    return answer