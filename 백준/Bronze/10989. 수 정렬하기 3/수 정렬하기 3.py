import sys

n = int(sys.stdin.readline())
count = [0] * 10001    # 0~10000까지 숫자 빈도수 저장

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1
    
for i in range(1, 10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
    