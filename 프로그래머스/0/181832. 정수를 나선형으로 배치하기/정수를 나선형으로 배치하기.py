def solution(n):
    result = [[0]*n for _ in range(n)]
    
    # 이동 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1] # 행, 세로 방향: 아래 & 위로만 움직임
    dy = [1, 0, -1, 0] # 열, 가로 방향: 우 & 좌로만 움직임
    direction = 0 # (dx[0], dy[0])부터 시작
    '''
    direction = 0 -> 오른쪽으로 이동
    direction = 1 -> 아래로 이동
    direction = 2 -> 왼쪽으로 이동
    direction = 3 -> 위로 이동
    '''
    
    x, y = 0, 0 # 시작 위치
    for num in range(1, n*n + 1):
        result[x][y] = num
    
        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]
        
        # 다음 위치가 범위를 벗어나거나, 이미 채워졌으면 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or result[nx][ny] != 0:
            direction = (direction + 1) % 4 # 방향 전환
            nx, ny = x + dx[direction], y + dy[direction] # 새 방향으로 다시 이동 계산
            
        # 실제 이동
        x, y = nx, ny
    
    return result