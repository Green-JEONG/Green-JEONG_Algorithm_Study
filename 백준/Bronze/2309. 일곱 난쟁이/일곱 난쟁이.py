from itertools import combinations

height = []

for _ in range(9):
    height.append(int(input()))
    
for comb in combinations(height, 7):
    if sum(comb) == 100:
        for i in sorted(comb):
            print(i)
        break