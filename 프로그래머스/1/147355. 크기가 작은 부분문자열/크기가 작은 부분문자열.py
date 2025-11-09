def solution(t, p):
    length = len(p)
    cnt = 0

    for i in range(len(t) - length+1): # i는 0부터 len(t) - length 까지만 돌아야 함
        num = int(t[i:i+length])
        
        if num <= int(p):
            cnt += 1
            
    return cnt