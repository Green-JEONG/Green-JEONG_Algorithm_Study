import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    lcm = a * b // math.gcd(a, b)
    print(lcm)