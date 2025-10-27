def solution(num):
    if num == 1:
        return 0
    
    cnt = 0
    
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1 # 계산 순서 주의
        cnt += 1

        if cnt >= 500:
            return -1
        
    return cnt