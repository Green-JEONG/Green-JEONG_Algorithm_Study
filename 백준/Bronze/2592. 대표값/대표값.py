from collections import Counter

total = 0
nums = []

for _ in range(10):
    n = int(input())
    total += n
    nums.append(n)
    
mean = total // 10
mode = Counter(nums).most_common(1)

print(mean)
print(mode[0][0])