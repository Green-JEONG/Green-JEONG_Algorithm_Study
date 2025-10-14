def solution(numbers, n):
    total = 0
    
    for num in numbers:
        if total > n:
            break
        total += num
            
    return total