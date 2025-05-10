import sys

t = int(sys.stdin.readline().rstrip())

for x in range(1, t + 1):
    a, b = map(int, sys.stdin.readline().split())
    
    print(f"Case {x}: {a + b}")