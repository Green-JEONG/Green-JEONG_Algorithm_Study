import sys

n = int(sys.stdin.readline())
line = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    line.append((age, name))
    
line.sort(key=lambda x: x[0])

for age, name in line:
    print(age, name)