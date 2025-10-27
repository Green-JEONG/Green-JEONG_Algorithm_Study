import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = 0
    
    i = max(n, m)
    while True:
        if i % n == 0 and i % m == 0:
            lcm = i
            break
        else:
            i += 1
    
    return [gcd, lcm]