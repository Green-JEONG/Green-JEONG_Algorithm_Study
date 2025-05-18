t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    result = sorted(a)[-3]
    print(result)
    