def solution(n, left, right):
    a = []
    s = [(left//n), (left%n)]
    e = [(right//n), (right%n)]
    while True:
        if s[1] < n:
            a.append(max(s[0], s[1])+1)
            s[1] = s[1]+1
        else:
            s[1] = 0
            s[0] = s[0]+1

        if (s[0]*n)+s[1] == right:
            a.append(max(s[0], s[1])+1)
            return a