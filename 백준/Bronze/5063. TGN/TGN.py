n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())
    if e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")
    else:
        print("does not matter")