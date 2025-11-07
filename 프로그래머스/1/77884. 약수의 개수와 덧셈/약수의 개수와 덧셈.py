def solution(left, right):
    total = 0
    
    for i in range(left, right+1):
        
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        # return cnt
        if cnt % 2 == 0:
            total += i
        else:
            total -= i
                    
    return total