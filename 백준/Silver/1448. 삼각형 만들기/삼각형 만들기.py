import sys
input = sys.stdin.readline

n = int(input())
lengths = [int(input()) for _ in range(n)]

lengths.sort(reverse=True)

# 가장 긴 변 < 나머지 두 변 합
for i in range(n - 2): # 뒤에서 순서 센다고 생각
    a, b, c = lengths[i], lengths[i + 1], lengths[i + 2]
    if a < b + c:
        print(a + b + c)
        break
else: # for 안에서 break가 한 번이라도 실행되면 else 건너뜀
    print(-1)