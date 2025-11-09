def solution(n):
    temp = []
    
    while n > 0:
        temp.append(n % 3)
        n //= 3
        
    result = 0
    for i in range(len(temp)):
        result += temp[i] * (3 ** (len(temp)-1-i))
        
    return result