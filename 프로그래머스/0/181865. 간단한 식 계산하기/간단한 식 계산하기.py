def solution(binomial):
    binomial = binomial.split()
    
    total = 0

    # 한 번만 계산하면 되므로 반복문 X
    if binomial[1] == '+':
        total += int(binomial[0]) + int(binomial[2])
    elif binomial[1] == '-':
        total += int(binomial[0]) - int(binomial[2])
    else:
        total += int(binomial[0]) * int(binomial[2])
        
    return total