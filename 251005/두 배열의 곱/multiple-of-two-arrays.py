matrix = [list(map(int, input().split())) for _ in range(3)]
input()
new_matrix = [list(map(int, input().split())) for _ in range(3)]

answer = []
for i in range(len(matrix)):
    row = []
    for j in range(len(new_matrix)):
        row.append(matrix[i][j] * new_matrix[i][j])
    answer.append(row)

for row in answer:
    print(*row)