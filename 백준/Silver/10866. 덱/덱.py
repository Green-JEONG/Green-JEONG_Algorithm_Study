import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

dq = deque()

for _ in range(n):
    order = input().rstrip()
    
    if "push_front" in order:
        _, x = order.split()
        dq.appendleft(int(x))
        
    elif "push_back" in order:
        _, x = order.split()
        dq.append(int(x))
        
    elif order == "pop_front":
        print(dq.popleft() if dq else -1)
        
    elif order == "pop_back":
        print(dq.pop() if dq else -1)
        
    elif order == "size":
        print(len(dq))
        
    elif order == "empty":
        print(0 if dq else 1)
        
    elif order == "front":
        print(dq[0] if dq else -1)
        
    elif order == "back":
        print(dq[-1] if dq else -1)