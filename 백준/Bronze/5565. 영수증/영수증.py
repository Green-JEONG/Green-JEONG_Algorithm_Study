import sys

total = int(sys.stdin.readline())
sum = 0

for _ in range(9):
    price = int(sys.stdin.readline())
    sum += price
    
print(total - sum)