import sys
import heapq

heap = []

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)