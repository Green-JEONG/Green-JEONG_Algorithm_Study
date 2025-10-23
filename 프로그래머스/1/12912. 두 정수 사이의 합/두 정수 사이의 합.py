def solution(a, b):
    total = 0
    
    if a <= b:
        for n in range(a, b+1):
            total += n
    else:
        for n in range(b, a+1):
            total += n
        
    return total