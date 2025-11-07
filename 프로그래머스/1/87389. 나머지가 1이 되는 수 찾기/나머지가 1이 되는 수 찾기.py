def solution(n):
    result = []
    
    for x in range(1, n+1):
        if n % x == 1:
            result.append(x)
            
    return result[0]
