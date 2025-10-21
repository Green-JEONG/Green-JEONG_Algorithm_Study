def solution(arr, k):
    result = []
    
    for n in arr:
        if n not in result:
            result.append(n)
        if len(result) == k:
            break
            
    while len(result) < k:
        result.append(-1)
        
    return result