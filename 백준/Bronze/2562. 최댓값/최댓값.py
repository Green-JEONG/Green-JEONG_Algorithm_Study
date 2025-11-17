nums = []

for _ in range(9):
    n = int(input())
    nums.append(n)

max_num = max(nums)
print(max_num)
print(nums.index(max_num) + 1)