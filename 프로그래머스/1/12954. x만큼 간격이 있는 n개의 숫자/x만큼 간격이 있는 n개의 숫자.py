def solution(x, n):
    answer = []
    
    ''' 우연히 테스트 케이스가 맞은 것뿐, 양/음수로 분기하지 않아도 해결 가능
    if x > 0:
        for i in range(x, x*n+1, x):
            answer.append(i)
    else:
        for i in range(x, x*n-1, x):
            answer.append(i)
    '''
    
    for i in range(1, n+1):
        answer.append(x * i)
            
    return answer