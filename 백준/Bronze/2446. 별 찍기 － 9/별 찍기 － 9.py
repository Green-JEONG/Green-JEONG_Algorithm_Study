import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * (2 * (n - i) + 1))
    
for i in range(n - 1, 0, -1):
    print(" " * (i - 1) + "*" * (2 * (n - i) + 1))