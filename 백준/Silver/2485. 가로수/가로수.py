import sys
import math

input = sys.stdin.readline

n = int(input())
trees = [int(input()) for _ in range(n)]

gaps = []
for i in range(1, n):
    gaps.append(trees[i] - trees[i - 1])

gcd_gaps = gaps[0]
for gap in gaps[1:]:
    gcd_gaps = math.gcd(gcd_gaps, gap)
    
count = 0
for gap in gaps:
    count += (gap // gcd_gaps) - 1
    
print(count)