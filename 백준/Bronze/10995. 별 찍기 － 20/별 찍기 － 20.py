import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)