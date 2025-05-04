s = int(input())
n = 1
sum = 0

while 1:
    sum += n
    if sum > s:
        break
    n += 1
    
print(n - 1)