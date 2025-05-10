import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

sum = 0
prime_list = []

for i in range(m, n + 1):
    if i < 2:
        continue
    if i == 2:
        sum += i
        prime_list.append(i)
        continue
        
    for j in range(2, i):
        if i % j == 0:
            break  
    else:
        sum += i
        prime_list.append(i)
        
if len(prime_list) == 0:
        print(-1)
else:
    print(sum)
    print(prime_list[0])