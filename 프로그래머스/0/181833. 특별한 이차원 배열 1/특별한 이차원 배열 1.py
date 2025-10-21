def solution(n):
    arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 1
    
    return arr