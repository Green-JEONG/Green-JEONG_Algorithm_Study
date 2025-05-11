n = int(input())

scores = list(map(int, input().split()))

total = 0
streak = 0

for i in scores:
    if i == 1:
        streak += 1
        total += streak
    else:
        streak = 0
            
print(total)