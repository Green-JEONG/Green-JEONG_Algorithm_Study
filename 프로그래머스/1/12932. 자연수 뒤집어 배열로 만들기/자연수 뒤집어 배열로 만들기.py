def solution(n):
    result = []
    
    for x in str(n):
        result.append(int(x))
    
    return result[::-1]