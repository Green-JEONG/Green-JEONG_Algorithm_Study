import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    total_credit = 0
    total_gpa = 0.0
    
    for _ in range(n):
        c, g = sys.stdin.readline().split()
        c = int(c)
        g = float(g)
        
        total_credit += c
        total_gpa += c * g
        
    result = total_gpa / total_credit
    print(total_credit, result)