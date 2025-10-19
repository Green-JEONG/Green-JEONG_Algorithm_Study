def solution(arr, k):
    result = []
    
    for n in arr:
        if k % 2 == 1:
            result.append(n*k)
        else:
            result.append(n+k)
            
    return result