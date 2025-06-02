import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n + 1) # 감염시, True로 전환

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    count = 0
    
    while q: # 큐에 처리할 컴퓨터 남아있으면 반복
        v = q.popleft() # 큐에서 computer 하나 꺼내 번호 저장
        for i in graph[v]: # computer 번호와 연결된 이웃 꺼내기
            if not visited[i]:
                q.append(i) # 전파할 가능성 있는 감염된 컴퓨터
                visited[i] = True
                count += 1
    return count

print(bfs(graph, 1, visited))