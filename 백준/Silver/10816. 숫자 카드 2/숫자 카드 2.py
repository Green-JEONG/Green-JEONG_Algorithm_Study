import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dict = {}
for i in cards:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
m = int(input())
nums = list(map(int, input().split()))

result = []
for num in nums:
    result.append(str(dict.get(num, 0)))
    
print(' '.join(result))