from collections import deque

# 4방향 + 왼/오 4방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    
    while queue: # 큐에 남아있는게 O
        x, y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < w and 0 <= ny < h: # 지도 범위 내에 속하는지 확인
                if not visited[ny][nx] and graph[ny][nx] == 1: # 방문 X, 땅이면
                    visited[ny][nx] = True
                    queue.append((nx, ny))
                    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
        
    # 지도
    graph = [list(map(int, input().split())) for _ in range(h)] # 높이만큼 지도(2차원 리스트: 0-바다, 1-땅) 입력받기
    visited = [[False] * w for _ in range(h)] # 2차원 리스트 False로 초기화
    
    count = 0
    # 전체적으로 지도 한 칸씩 확인
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                count += 1
                
    print(count)