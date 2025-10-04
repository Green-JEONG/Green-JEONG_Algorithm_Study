f, s = map(int, input().split())
nums = [f, s]
for i in range(8):
    nums.append((nums[i] + nums[i+1]) % 10)
# while len(nums) < 10:
#     nums.append((nums[-2] + nums[-1]) % 10)
print(*nums)