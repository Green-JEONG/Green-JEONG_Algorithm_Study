def solution(d, budget): # 조합을 쓰면 시간 초과이므로 그리디 접근 필요
    d.sort() # 작은 금액부터 처리하면 더 많은 부서 처리 가능
    cnt = 0
    
    for n in d:
        if budget >= n:
            budget -= n
            cnt += 1
        else:
            break
            
    return cnt