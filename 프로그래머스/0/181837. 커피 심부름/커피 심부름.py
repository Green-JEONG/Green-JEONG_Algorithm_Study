def solution(order):
    total = 0
    
    for ch in order:
        if 'latte' in ch:
            total += 5000
        else:
            total += 4500
            
    return total