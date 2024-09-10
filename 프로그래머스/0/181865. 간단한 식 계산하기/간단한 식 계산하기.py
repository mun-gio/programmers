def solution(binomial):
    n1, sign, n2 = binomial.split(' ')
    n1 = int(n1)
    n2 = int(n2)
    if sign == '+':
        return n1+n2
    elif sign == '-':
        return n1-n2
    else:
        return n1*n2