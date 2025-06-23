import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append(u)
                
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1
        
print(count)