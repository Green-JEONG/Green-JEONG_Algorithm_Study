import sys

n = int(sys.stdin.readline().rstrip())

sum = 0

# 0 <= i <= j <= n
for i in range(n + 1):
    for j in range(i, n + 1):
        sum += i + j
    
print(sum)