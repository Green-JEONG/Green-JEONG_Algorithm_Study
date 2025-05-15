t = int(input())

for _ in range(t):
    n = int(input())
    xi = list(map(int, input().split()))
    
    xi.sort()
    
    total = 0
    
    for i in range(1, n):
        total += xi[i] - xi[i - 1]
        
    print(total + xi[-1] - xi[0])
        