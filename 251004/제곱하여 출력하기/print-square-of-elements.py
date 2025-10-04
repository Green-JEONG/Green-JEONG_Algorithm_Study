n = int(input())
nums = list(map(int, input().split()))
answer = [nums[i]**2 for i in range(len(nums))]
print(' '.join(map(str, answer)))

# print(*[x**2 for x in map(int, input().split())])