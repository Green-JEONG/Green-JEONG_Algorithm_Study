from itertools import combinations

nums =[]
for _ in range(9):
    nums.append(int(input()))
    
    for comb in combinations(nums, 7):
        if sum(comb) == 100:
            for i in comb:
                print(i)
            break