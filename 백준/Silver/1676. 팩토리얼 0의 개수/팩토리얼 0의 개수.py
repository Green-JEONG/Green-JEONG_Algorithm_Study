import math

n = int(input())
back = list(str(math.factorial(n)))[::-1]

count = 0
for i in back:
    if i == '0':
        count += 1
    else:
        break

print(count)