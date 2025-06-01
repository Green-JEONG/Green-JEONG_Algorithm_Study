def solution(order):
    total = 0
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            total += 1
        
    return total