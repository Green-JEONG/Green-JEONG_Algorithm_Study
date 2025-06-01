import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

q = deque()

for _ in range(n):
    order = input().rstrip()
    
    if "push" in order:
        _, value = order.split()
        q.append(int(value))
        
    elif order == "pop":
        if q:
            print(str(q.popleft()))
        else:
            print("-1")
            
    elif order == "size":
        print(str(len(q)))
        
    elif order == "empty":
        print('1' if not q else '0')
        
    elif order == "front":
        if q:
            print(str(q[0]))
        else:
            print("-1")
            
    elif order == "back":
        if q:
            print(str(q[-1]))
        else:
            print("-1")