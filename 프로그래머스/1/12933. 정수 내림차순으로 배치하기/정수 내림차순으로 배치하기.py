def solution(n):
    digits = []
    
    for x in str(n):
        digits.append(x)
        
    digits.sort(reverse=True)
        
    return int(''.join(digits))