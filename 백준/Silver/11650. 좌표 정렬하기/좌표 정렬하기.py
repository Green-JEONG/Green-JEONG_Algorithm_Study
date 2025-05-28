import sys

n = int(sys.stdin.readline())

dots = []
for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))
    
sorted_dots = sorted(dots, key=lambda x: (x[0], x[1]))

for dot in sorted_dots:
    print(dot[0], dot[1])
    