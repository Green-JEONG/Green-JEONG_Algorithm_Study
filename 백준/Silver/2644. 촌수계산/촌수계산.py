from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph  = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False] * (n + 1)

# 촌수 저장
distance = [0] * (n + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if not visited[g]:
                visited[g] = True
                distance[g] = distance[now] + 1
                queue.append(g)
                
bfs(a)

if distance[b] != 0:
    print(distance[b])
elif a == b:
    print(0)
else:
    print(-1)