import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
new_b = sorted(b, reverse = True)

s = sum(a * b for a, b in zip(a, new_b))
print(s)