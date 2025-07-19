def solution(s):
    result = []
    
    for i in s:
        if s.count(i) == 1:
            result.append(i)
            
    result.sort()
    
    return ''.join(result)