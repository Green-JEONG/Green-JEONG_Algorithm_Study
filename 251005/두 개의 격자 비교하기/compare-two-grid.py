n, m = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]

answer = []

for i in range(n):
    row = []
    for j in range(m):
        if matrix1[i][j] == matrix2[i][j]:
            row.append(0)
        else:
            row.append(1)
    answer.append(row)

for row in answer:
    print(*row)