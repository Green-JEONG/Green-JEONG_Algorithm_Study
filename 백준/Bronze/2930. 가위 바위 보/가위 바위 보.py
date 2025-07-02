r = int(input())
s_shapes = input().rstrip() 
n = int(input())
f_shapes = [input().rstrip() for _ in range(n)]

def versus(s, f):
    if s == f:
        return 1
    elif (s == 'S' and f == 'P') or (s == 'P' and f == 'R') or (s == 'R' and f == 'S'):
        return 2
    else:
        return 0

score = 0
for i in range(r):
    for j in range(n):
        score += versus(s_shapes[i], f_shapes[j][i])

max_score = 0
for i in range(r):
    total = 0
    for shape in ['S', 'P', 'R']:
        temp = 0
        for j in range(n):
            temp += versus(shape, f_shapes[j][i])
        total = max(total, temp)
    max_score += total

print(score)
print(max_score)