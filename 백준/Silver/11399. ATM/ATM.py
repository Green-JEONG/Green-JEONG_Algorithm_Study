n = int(input())
p = list(map(int, input().split()))

p.sort()

min = 0
total = 0

for time in p:
    total += time
    min += total

print(min)