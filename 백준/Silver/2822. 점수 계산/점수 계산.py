scores = []

for i in range(8):
    score = int(input())
    scores.append((score, i + 1))

top5 = sorted(scores, reverse=True)[:5]

total = 0
for s in top5:
    total += s[0]

n = []
for s in top5:
    n.append(s[1])
n.sort()

print(total)
print(*n)