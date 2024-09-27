def solution(s):
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, sn in enumerate(num_list):
        if sn in s:
            s = s.replace(sn, str(i))
    return int(s)