def solution(s):
    num = 0
    zero = 0
    while True:
        if 1 != len(s):
            zero += s.count('0')
            s = s.replace("0","")
            s = len(s)
            s = bin(s).replace('0b','')
            num += 1
        else:
            return [num, zero]