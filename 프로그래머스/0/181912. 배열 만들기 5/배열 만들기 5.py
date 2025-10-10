def solution(intStrs, k, s, l):
    result = []
    
    for x in intStrs:
        temp = int(x[s:s+l])
        if temp > k:
            result.append(temp)
            
    return result