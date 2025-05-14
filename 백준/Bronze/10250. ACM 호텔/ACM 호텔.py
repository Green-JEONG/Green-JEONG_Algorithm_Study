t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    
    if h < n:
        floor = n % h
        room = n // h + 1
        if floor == 0:
            floor = h
            room = n // h
    elif h == n:
        floor = h
        room = 1
    else:
        floor = n
        room = 1
    
    print(f"{floor}{room:02d}")