max_n = 0
max_total = 0

for i in range(5):
    scores = list(map(int, input().split()))
    total = sum(scores)
    
    if total > max_total:
        max_total = total
        max_n = i + 1
            
print(max_n, max_total)