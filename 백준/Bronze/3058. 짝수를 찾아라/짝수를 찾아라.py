t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    even = [n for n in nums if n % 2 == 0]
    print(sum(even), min(even))