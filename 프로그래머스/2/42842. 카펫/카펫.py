def solution(brown, yellow):
    for h in range(1,(brown+yellow)//2):
        if (brown+yellow)%h == 0:
            w = (brown+yellow)//h
        else:
            continue
        if brown == (w*2) + ((h-2)*2) and yellow == ((w-2)*(h-2)):
            return [w,h]
            