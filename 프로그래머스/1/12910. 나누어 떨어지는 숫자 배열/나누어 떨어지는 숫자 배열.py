def solution(arr, divisor):
    result = []
    
    for n in arr:
        if n % divisor == 0:
            result.append(n)
    
    if not result:
        return [-1]
    
    return sorted(result)