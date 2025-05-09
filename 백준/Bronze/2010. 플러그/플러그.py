import sys

n = int(sys.stdin.readline().rstrip())
sum = 0

for _ in range(n):
    c = int(sys.stdin.readline().rstrip())
    sum += c
    
# 전체 플러그 수 - (멀티탭 개수 - 1)
print(sum - (n - 1))