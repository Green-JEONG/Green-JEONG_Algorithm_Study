n = int(input())
nums = list(map(int, input().split()))

if len(nums) == 1:
    print(nums[0] ** 2)
elif len(nums) > 1:
    print(min(nums) * max(nums))