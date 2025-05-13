total = 0
max_total = 0

for _ in range(10):
    off, on = map(int, input().split())

    total += on - off
    
    if total > max_total:
        max_total = total
        
print(max_total)