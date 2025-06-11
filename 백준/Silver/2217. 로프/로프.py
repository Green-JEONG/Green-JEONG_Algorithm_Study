import sys

input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort(reverse=True)

max_w = 0
for i in range(n):
    w = ropes[i] * (i + 1)
    max_w = max(max_w, w)
    
print(max_w)