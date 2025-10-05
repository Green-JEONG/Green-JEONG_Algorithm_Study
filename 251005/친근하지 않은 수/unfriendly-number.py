n = int(input())
total = 0
for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    total += 1
print(total)