def solution(s):
    s_num = [int(num) for num in s.split(" ")]
    return str(min(s_num)) + " " + str(max(s_num))