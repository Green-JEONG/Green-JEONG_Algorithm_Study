def solution(n):
    total = 0
    
    for n in str(n):
        total += int(n)
        
    return total
    # return sum(int(n) for n in str(n))