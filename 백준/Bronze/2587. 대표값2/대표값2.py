a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mean = (a + b + c + d + e) // 5
median = sorted([a, b, c, d, e])[2]

print(mean)
print(median)