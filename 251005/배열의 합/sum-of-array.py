# for _ in range(4):
#     total = 0
#     nums = map(int, input().split())
#     total += sum(nums)
#     print(total)

matrix = [list(map(int, input().split())) for _ in range(4)]

for row in matrix:
    total = 0
    for num in row:
        total += num
    print(total)