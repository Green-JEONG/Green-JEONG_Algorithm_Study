k = int(input())

for _ in range(k):
    p, m = list(map(int, input().split()))
    
    n = []
    for _ in range(p):
        n.append(int(input()))
    
    result = len(n) - len(set(n))
    print(result)