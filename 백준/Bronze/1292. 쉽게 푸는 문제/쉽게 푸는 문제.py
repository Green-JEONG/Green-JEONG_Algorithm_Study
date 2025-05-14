a, b = map(int, input().split())

s = []
n = 1

while len(s) < b:
    s += [n] * n
    n += 1
    
print(sum(s[a - 1:b]))