def solution(picture, k):
    result = []
    
    for row in picture:
        temp = ''
        
        for ch in row:
            temp += ch * k
            
        for _ in range(k):
            result.append(temp)
            
    return result