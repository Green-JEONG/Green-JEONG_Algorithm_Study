n = int(input())
nums = map(int, input().split())
answer = []
for num in nums:
    if num % 2 == 0:
        answer.append(num)
answer.reverse()
print(' '.join(map(str, answer)))