import sys

n = int(sys.stdin.readline())
remain = 0

for _ in range(n):
    s, a = map(int, sys.stdin.readline().split())
    
    remain += a % s
    
print(remain)