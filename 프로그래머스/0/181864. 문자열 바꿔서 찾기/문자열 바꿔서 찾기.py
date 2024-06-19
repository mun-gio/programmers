def solution(myString, pat):
    if pat.lower() in myString.replace("A","b").replace("B","a"):
        return 1
    return 0