import sys

n = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for c in check:
    if c in nums:
        print(1)
    else:
        print(0)