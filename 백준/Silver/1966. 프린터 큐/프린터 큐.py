from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    
    queue = deque((l, p) for l, p in enumerate(prior)) # (문서 위치, 중요도)
    count = 0 # 인쇄 순서
    
    while queue:
        d = queue.popleft()
        if any(d[1] < q[1] for q in queue): # 중요도가 더 높은 문서가 하나라도 존재하면
            queue.append(d) # 인쇄 안 하고, 큐 맨 뒤로
        else:
            count += 1
            if d[0] == m:
                print(count)
                break