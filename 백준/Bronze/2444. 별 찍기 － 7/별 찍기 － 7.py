import sys

n = int(sys.stdin.readline())

# 반으로 나눈 위쪽
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
# 반으로 나눈 아래쪽
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))