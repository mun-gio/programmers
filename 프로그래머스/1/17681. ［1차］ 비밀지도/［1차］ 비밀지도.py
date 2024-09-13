def solution(n, arr1, arr2):
    answer = []
    
    dtc = {"0":" ","1":"#"}
    
    for i in range(n):
        answer.append(format(arr1[i] | arr2[i] ,'b'))
    
    
    for key, value in dtc.items():
        for i in range(n):
            answer[i] = answer[i].zfill(n)
            answer[i] = answer[i].replace(key,value)
    
        
        
    return answer