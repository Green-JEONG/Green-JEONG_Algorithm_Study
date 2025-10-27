def solution(x):
    total = 0
    
    for n in str(x):
        total += int(n)
        
    return x % total == 0