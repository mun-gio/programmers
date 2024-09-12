def solution(brown, yellow):
    for h in range(1,(brown+yellow)//2):
        w = (brown+yellow)//h
        if brown == (w*2) + ((h-2)*2) and yellow == ((w-2)*(h-2)):
            return [w,h]
            