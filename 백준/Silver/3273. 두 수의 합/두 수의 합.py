n = int(input())
nums = list(map(int, input().split()))
x = int(input())

cnt = 0
seen = set()

for num in nums:
    if x - num in seen:
        cnt += 1
    seen.add(num)
    
print(cnt)