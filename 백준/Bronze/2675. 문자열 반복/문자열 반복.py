t = int(input())
for _ in range(t):
    r, s = input().split()
    result = ""
    for i in s:
        result += i * int(r)
    print(result)