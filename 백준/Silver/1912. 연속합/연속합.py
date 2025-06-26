n = int(input())
nums = list(map(int, input().split()))

total = max_total = nums[0]

for i in range(1, n):
    total = max(nums[i], total + nums[i])
    max_total = max(max_total, total)
    
print(max_total)