from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
x = []

while queue:
    queue.rotate(-(k - 1)) # 왼쪽 회전
    x.append(queue.popleft())
    
print("<" + ", ".join(map(str, x)) + ">")