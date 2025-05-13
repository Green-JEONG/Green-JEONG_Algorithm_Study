t = int(input())

for _ in range(t):
    n, s = input().split()
    
    n = int(n)
    s = list(s)
    
    s.pop(n - 1)
    print("".join(s))