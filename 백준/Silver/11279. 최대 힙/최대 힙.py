import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 음수에 음수 붙여 가장 큰 값 출력
        else: # 비어 있으면
            print(0)
    else:
        heapq.heappush(heap, -x) # 최대 힙 사용위해 음수로