import sys

n = int(sys.stdin.readline())

nums = set()
for _ in range(n):
    nums.add(int(sys.stdin.readline()))
    
nums = sorted(nums)

for num in nums:
    print(num)