def solution(board):
    n = len(board)
    danger = [[False]*n for _ in range(n)]  # 위험 지역 표시용
    
    # 자기 자신 포함한 8방향 (총 9칸)
    dirs = [(-1,-1), (-1,0), (-1,1),
            ( 0,-1), ( 0,0), ( 0,1),
            ( 1,-1), ( 1,0), ( 1,1)]

    # 지뢰(1) 발견 시, 주변 8칸+자기자신을 위험 처리
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = True

    # 위험이 아닌 칸(= 안전 칸) 세기
    safe = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                safe += 1

    return safe