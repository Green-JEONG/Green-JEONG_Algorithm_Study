from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for g in graph:
    g.sort()
    
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, start, visited):
    queue = deque([start])
    
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
visited = [False] * (n + 1)
dfs(graph, v, visited)

print() # 줄바꿈

visited = [False] * (n + 1)
bfs(graph, v, visited)